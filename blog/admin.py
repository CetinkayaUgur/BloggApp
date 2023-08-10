from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = [
        'pk',
        'title',
        'is_deleted',
        'created_at',
        'updated_at',
    ]

    list_display_links = [
        'pk',
        'title',
    ]

admin.site.register(Post, PostAdmin)

# class UserAdmin(admin.ModelAdmin):
#     list_display = [
#         'pk',
#         'user_name',
#         'first_name',
#         'last_name',
#         'email',
#         'password',
#     ]

#     list_display_links = [
#         'pk',
#         'user_name',
#         'first_name',
#         'last_name',
#     ]

# admin.site.register(User, UserAdmin)