# from django.contrib import admin

# Register your models here.


from django.contrib import admin

from .models import Profile, Comment, Caption, Follow

# Register your models here.
admin.site.register(Profile)
admin.site.register(Comment)
admin.site.register(Caption)
admin.site.register(Follow)

