from django.contrib import admin
from .models import Post, City, Comment
# Register your models here.


admin.site.register(Post)
admin.site.register(City)
admin.site.register(Comment)