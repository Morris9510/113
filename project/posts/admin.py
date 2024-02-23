from django.contrib import admin
from django.contrib.admin import ModelAdmin
from .models import Post

class PostAdmin(ModelAdmin):
    list_display = ["title", "subtitle", "body"]

admin.site.register(Post, PostAdmin)


# Register your models here.
