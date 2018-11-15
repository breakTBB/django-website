import xadmin
from .models import Blog, BlogType

class BlogTypeAdmin(object):
    list_display = ['type_name']
    search_fields= ['type_name']

class BlogAdmin(object):
    list_display = ['title', 'blog_type', 'content', 'author']


xadmin.site.register(BlogType, BlogTypeAdmin)
xadmin.site.register(Blog, BlogAdmin)