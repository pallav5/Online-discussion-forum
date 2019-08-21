from django.contrib import admin
from .models import Post,Comment,Category


# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_display = ('user','title','id','date','category')

admin.site.register(Post,PostAdmin)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'post','Email')
    actions = None


admin.site.register(Comment,CommentAdmin)



class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title',)


admin.site.register(Category,CategoryAdmin)



