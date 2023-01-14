from django.contrib import admin
from .models import Post
# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ('title','author','content','created_on',
    'category','images')
    list_filter=('category',)
    search_fields = ('title','content',)
    
admin.site.register(Post,PostAdmin)