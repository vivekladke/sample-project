from django.db import models
from django.contrib.auth.models import User


# User Login Information Table
class UserLoginProfile(models.Model):
    # Links UserLoginProfile to a User model instance.
    user = models.OneToOneField(User)

    # The adding Mobile Number
    mobileNumber = models.CharField(max_length=10)

    # Adding fields to maintain user logs
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(blank=True, null=True,
                                      default=None, db_index=True)
    deleted_on = models.DateTimeField(blank=True, null=True,
                                      default=None, db_index=True)
