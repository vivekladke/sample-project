from django_extensions.db.fields import UUIDField
from django.contrib.auth.models import User
from django.db import models


# User Login Information Table
class UserLoginProfile(models.Model):
    id = UUIDField(version=4, primary_key=True)
    # Links UserLoginProfile to a User model instance.
    user = models.OneToOneField(User)

    # The adding Mobile Numbaer
    mobileNumber = models.CharField(max_length=10)

    # Adding fields to maintain user logs
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(blank=True, null=True,
                                      default=None, db_index=True)
    deleted_on = models.DateTimeField(blank=True, null=True,
                                      default=None, db_index=True)
