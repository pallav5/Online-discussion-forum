
from django.urls import path


from forum import views



urlpatterns = [


    path('view/',views.PostList,name='post_list'),
    # path('category/(<slug:slug>).html/',views.view_category,name='view_category'),
    # path('detail/comment/<int:id>',views.add_comment,name='add_comment'),
    path('category/<int:id>/', views.list_of_post_by_category, name='list_of_post_by_category'),
    path('detail/<int:id>/', views.PostDetail, name='post_detail'),
    path('category/detail/<int:id>/', views.CategoryDetail, name='category_detail'),
    path('post/new/', views.new_post, name='new_post'),
    path('category/new/add/', views.add_category, name='add_category'),
    path('category/all/list/', views.CategoryList, name='category_list'),
    path('post/all/', views.PostListAll, name='post_list_all'),
    path('signup/', views.signup, name='signup'),
    path('signin/', views.signin, name='login'),
    path('logout/', views.mylogout, name='logout'),
    path('post/<int:id>/edit/', views.edit_post, name='edit_post'),
    path('category/<int:id>/edit/', views.edit_category, name='edit_category'),
    path('comment/edit/<int:id>/', views.edit_comment, name='edit_comment'),
    path('reply/edit/<int:id>/', views.edit_reply, name='edit_reply'),
    path('comment/delete/<int:id>/', views.delete_comment, name='delete_comment'),
    path('reply/delete/<int:id>/', views.delete_reply, name='delete_reply'),
    path('post/<int:id>/delete/', views.delete_post, name='delete_post'),
    path('category/<int:id>/delete/', views.delete_category, name='delete_category'),
    path('vote/<int:id>/', views.vote_comment, name='vote_comment'),


]