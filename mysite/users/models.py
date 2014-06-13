from django.db import models
from django.contrib.auth.models import User

# test table
class test_tab(models.Model):
    company_name = models.CharField(max_length=200)
    
    def __unicode__(self):
        return self.company_name

# User Login Information Table  
class UserLoginProfile(models.Model):
    # Links UserLoginProfile to a User model instance.
    user = models.OneToOneField(User)

    # The adding Mobile Numbaer
    mobileNumber = models.CharField(max_length=10)

    # Adding fields to maintain user logs
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(blank=True, null=True,default=None,db_index=True)
    deleted_on = models.DateTimeField(blank=True, null=True, default=None,db_index=True)


    
