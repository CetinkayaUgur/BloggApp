from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(blank=True, null=True)
    description = models.TextField(max_length=1000000)
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
# class User(models.Model):
#     user_name   = models.CharField(max_length=50,unique=True)
#     first_name = models.CharField(max_length=50)
#     last_name = models.CharField(max_length=50)
#     email  = models.EmailField(max_length=70,unique=True)
#     password = models.CharField(max_length=50)

#     def __str__(self):
#         return self.user_name
    
