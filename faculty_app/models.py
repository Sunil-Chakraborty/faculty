from django.db import models
import uuid
from ckeditor.fields import RichTextField

# Create your models here.

class Faculty(models.Model):    
    username        = models.CharField("Full Name",max_length=200)
    profile_image   = models.ImageField(blank=True, null=True, upload_to='profiles/', default="profiles/user-default.png")
    email           = models.EmailField("Email_ID",max_length=500)
    pwd             = models.CharField("Password",max_length=50)
    department      = models.ManyToManyField('Department',max_length=200)
    location        = models.CharField(max_length=200, blank=True, null=True)
    short_intro     = models.CharField(max_length=200, blank=True, null=True)
    bio             = models.TextField(blank=True, null=True)
    created         = models.DateTimeField(auto_now_add=True)
    id              = models.UUIDField(default=uuid.uuid4, unique=True,
                      primary_key=True, editable=False)
    
    def __str__(self):
        return self.username

class Department(models.Model):
    dept_name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return self.dept_name     
