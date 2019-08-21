from django.db import models
from django.utils import timezone
from django.conf import settings
from django.contrib.auth.models import User


from django.utils.text import slugify
from django.urls import reverse


# from django.urls import reverse

import time
# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=100,unique=True)

    date = models.DateField(default = timezone.now)
    user = models.ForeignKey(User,on_delete= models.CASCADE)

    class Meta:
        # ordering = ('title')
        verbose_name = 'category'
        verbose_name_plural = 'categories'


    # def get_absolute_url(self):
    #     return reverse('forum:list_of_post_by_category', args=[self.slug])
    def __str__(self):
        return self.title

class Post(models.Model):
    title = models.CharField(max_length=30,unique=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


    desc = models.TextField()
    date = models.DateTimeField(null=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE,null=True)


    class Meta:
        ordering = ['-date']
        verbose_name = 'post'
        verbose_name_plural = 'posts'

    def __str__(self):
        return self.title





class Comment(models.Model):

    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name='comments')
    content = models.TextField()
    date = models.DateTimeField(null=True,auto_now_add=True)
    Email = models.EmailField()
    votes = models.ManyToManyField(User,related_name='votes',blank=True)

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    reply = models.ForeignKey('Comment', null=True,on_delete=models.CASCADE, blank=True, related_name='replies')
    # user_comments = models.ForeignKey(User, related_name='comments', null=True,on_delete=models.CASCADE())


    class Meta:
        ordering = ['-date']
        verbose_name = 'comment'


    def __str__(self):
        return self.user

    def get_absolute_url(self):
        return reverse("post_detail",args=[self.id])










