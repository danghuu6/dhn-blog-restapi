from django.contrib import admin
from .models import Comment, Categories, User, Posts
# Register your models here.


admin.site.register(Posts)
admin.site.register(Comment)
admin.site.register(Categories)
admin.site.register(User)

