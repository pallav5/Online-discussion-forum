from django.shortcuts import render, redirect, get_object_or_404, render_to_response,HttpResponseRedirect,HttpResponse
from forum.forms import CommentForm, PostForm, CategoryForm
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import PermissionDenied
from django.contrib import messages
from django.views.generic import RedirectView
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .models import Post, Comment
from .models import Category


def index(request):
    return render_to_response('forum/post_list.html', {
        'categories': Category.objects.all(),
        'posts': Post.objects.all()[:5]
    })


@login_required(login_url='login')
def PostList(request):
    post = Post.objects.all()

    context = {'post': post}
    return render(request, 'forum/post_list.html', context)


def PostListAll(request):
    post = Post.objects.all()

    context = {'post': post}
    return render(request, 'forum/post_list_all.html', context)


def CategoryList(request):
    category = Category.objects.all()

    context = {'category': category}
    return render(request, 'forum/category_list.html', context)


@login_required(login_url='login')
def PostDetail(request,id):
    post = get_object_or_404(Post, pk=id)
    comments = Comment.objects.filter(post=post,reply=None).order_by('-id')
    # comment = get_object_or_404(Comment, pk=id)
    # voted = False
    # if comment.votes.filter(id=request.user.id).exists():
    #     voted = True


    if request.method == 'POST':
        comment_form = CommentForm(request.POST or None)
        if comment_form.is_valid():
            reply_id = request.POST.get('comment_id')
            comment_as = None
            if reply_id:
                comment_as = Comment.objects.get(id=reply_id)
            comment = comment_form.save(commit=False)
            comment.user = request.user
            comment.post = post
            comment.reply = comment_as
            comment.save()
            return redirect('post_detail',id=post.id)
    else:
        comment_form = CommentForm()
    context = {'comment_form': comment_form,'post':post,'comments':comments,}
    return render(request, 'forum/post_detail.html', context)



@login_required(login_url='login')
def CategoryDetail(request, id):
    category = get_object_or_404(Category, pk=id)

    context = {'category': category}

    return render(request, 'forum/category_detail.html', context)


@login_required(login_url='login')
def list_of_post_by_category(request, id):
    category = get_object_or_404(Category, pk=id)
    post = Post.objects.filter(category=category)

    context = {'category': category, 'post': post}
    return render(request, 'forum/list_of_post_by_category.html', context)






def edit_post(request, id):
    post = get_object_or_404(Post, pk=id)
    if request.user == post.user:
        form = PostForm(request.POST or None, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            messages.success(request, "Post was modified")
            return redirect('post_list_all')
        context = {'form': form}
        return render(request, 'forum/new_post.html', context)
    else:
        raise PermissionDenied


def edit_category(request,id):
    category = get_object_or_404(Category, pk=id)
    if request.user == category.user:
        form = CategoryForm(request.POST or None, instance=category)
        if form.is_valid():
            category = form.save(commit=False)
            category.save()
            messages.success(request, "Post was modified")
            return redirect('category_list')
        context = {'form': form}
        return render(request, 'forum/add_category.html', context)
    else:
        raise PermissionDenied


def edit_comment(request,id):

    comment = get_object_or_404(Comment, pk=id)

    if request.user == comment.user:
        comment_form = CommentForm(request.POST or None,instance=comment)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.user = request.user
            comment.save()
            messages.success(request, "Comment was modified")
            return redirect('post_detail',id=comment.post_id)
        context = {'comment_form': comment_form}
        return render(request, 'forum/edit_comment.html', context)
    else:
        raise PermissionDenied



def edit_reply(request,id):

    reply = get_object_or_404(Comment, pk=id)

    if request.user == reply.user:
        comment_form = CommentForm(request.POST or None,instance=reply)
        if comment_form.is_valid():
            reply = comment_form.save(commit=False)
            reply.user = request.user
            reply.save()
            messages.success(request, "Comment was modified")
            return redirect('post_detail',id=reply.post_id)
        context = {'comment_form': comment_form}
        return render(request, 'forum/edit_comment.html', context)
    else:
        raise PermissionDenied




def delete_post(request,id):
    post = get_object_or_404(Post, pk=id)
    if request.user == post.user:
        post.delete()
        messages.success(request, "Successfully deleted")
        return redirect('post_list_all')
    raise PermissionDenied




def delete_comment(request,id):
    comment = get_object_or_404(Comment, pk=id)
    if request.user == comment.user:
        comment.delete()
        messages.success(request, "Successfully deleted")
        return redirect('post_detail',id=comment.post_id)
    raise PermissionDenied


def delete_reply(request,id):
    reply = get_object_or_404(Comment, pk=id)
    if request.user == reply.user:
        reply.delete()
        messages.success(request, "Successfully deleted")
        return redirect('post_detail',id=reply.post_id)
    raise PermissionDenied




def delete_category(request,id):
    category = get_object_or_404(Category, pk=id)
    if request.user == category.user:
        category.delete()
        messages.success(request, "Successfully deleted")
        return redirect('category_list')
    raise PermissionDenied


##NEW POST
@login_required(login_url='login')
def new_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('post_detail',id=post.id)
            # return redirect('post_detail', slug=post.slug)
    else:
        form = PostForm()
    context = {'form': form}
    return render(request, 'forum/new_post.html', context)


def add_category(request):
    if request.method == "POST":

        form = CategoryForm(request.POST)
        if form.is_valid():
            category = form.save(commit=False)
            category.user = request.user
            category.save()
            # return redirect('category_detail', slug=category.slug)
            return redirect('category_detail',id=category.id)
    else:
        form = CategoryForm()
    context = {'form': form, }
    return render(request, 'forum/add_category.html', context)


def signin(request):
    if request.method == 'GET':
        return render(request, 'forum/signin.html')
    else:
        u = request.POST.get('username')
        p = request.POST.get('password')
        user = authenticate(username=u, password=p)
        if user is not None:
            login(request, user)
            return redirect('post_list')
        return render(request, 'forum/signin.html', {'errmsg': 'Username and password doesnot match'})


def signup(request):
    if request.method == 'GET':
        context = {
            'form': UserCreationForm()
        }
        return render(request, 'forum/signup.html', context)
    else:
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    return render(request, 'forum/signup.html', {'form': form})


def mylogout(request):
    logout(request)
    return redirect('login')











def vote_comment(request,id):
    commment = get_object_or_404(Comment,pk=id)
    voted = False
    if commment.votes.filter(id=request.user.id).exists():
        commment.votes.remove(request.user)
        voted = False
    else:
        commment.votes.add(request.user)
        voted = True
        return redirect('post_detail', id=commment.id)
        # return HttpResponseRedirect(commment.get_absolute_url())
    return render(request,'forum/post_detail.html',{'voted':voted})
    