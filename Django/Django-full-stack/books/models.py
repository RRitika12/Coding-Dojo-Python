from __future__ import unicode_literals
from django.db import models
import re, bcrypt
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')


class UserManager(models.Manager):
    def validator(self, postData):
        errors = {}
        if (postData['first_name'].isalpha()) == False:
            if len(postData['first_name']) < 2:
                errors['first_name'] = "First name should be atleast 2 characters!"

        if (postData['last_name'].isalpha()) == False:
            if len(postData['last_name']) < 2:
                errors['last_name'] = "Last name should be atleast 2 characters!"

        if EMAIL_REGEX.match(postData['email']) == None:
            errors['email'] = "Email not valid!"

        if len(postData['password']) < 8:
            errors['password'] = "Password should be atleast 8 characters!"
        
        if postData['password'] != postData['pwd_confirmation']:
            errors['pwd_confirmation'] = "Password confirmation must match password."

        return errors
    
    def loginValidator(self, postData):
        user = User.objects.filter(email = postData['log_email'])
        errors = {}
        if not user:
            errors['email'] = "Email not valid!"
        if user and not bcrypt.checkpw(postData['log_password'].encode('utf8'), user[0].password.encode('utf8')):
            errors['password'] = "Invalid password!"
        return errors
    
    def bookValidator(self, postData):
        errors = {}
        if len(postData['title']) < 1:
            errors['title'] = "Title is required!"
            
        if len(postData['desc']) < 5:
            errors['desc'] = "Description should be atleast 5 characters!"
        return errors
        
    

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = UserManager()
    
class Book(models.Model):
    title = models.CharField(max_length = 255)
    desc = models.CharField(max_length = 255)
    uploader = models.ForeignKey(User, related_name = "uploaded_books")
    liked_users = models.ManyToManyField(User, related_name = "liked_books")
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = UserManager()