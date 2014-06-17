from django_extensions.db.fields import UUIDField
from django.db import models

STATUS_CHOICES = (
    ('A', 'Active'),
    ('I', 'Inactive'),
    )


class HostDetails(models.Model):
    '''
    id = UUIDField(version=4, primary_key=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(blank=True, null=True, default=None,
    db_index=True)
    deleted_on = models.DateTimeField(blank=True, null=True, default=None,
    db_index=True)
    '''
    status = models.CharField(max_length=255, choices=STATUS_CHOICES,
                                      default='I')
    host_name = models.CharField(max_length=255)
    database_name = models.CharField(max_length=255)
    user_name = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    port = models.CharField(max_length=4)
