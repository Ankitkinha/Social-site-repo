from django.contrib import admin
from .models import User, Post, Hashtag, PostHashtag, Follow, Comment, Like


# @admin.register(User)
# class UserAdmin(admin.ModelAdmin):
#     list_display = ('name', 'mobile_no', 'email', 'created_on', 'updated_on')
#     search_fields = ('name', 'email', 'mobile_no')
#     list_filter = ('created_on', 'updated_on')
#     ordering = ('-created_on',)

admin.site.register(User)
admin.site.register(Post)
admin.site.register(Hashtag)
admin.site.register(PostHashtag)
admin.site.register(Follow)
admin.site.register(Comment)
admin.site.register(Like)
