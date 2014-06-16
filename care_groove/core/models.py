from django_extensions.db.fields import UUIDField
from django.db import models


class DbRouting(models.Model):
    id = UUIDField(version=4, primary_key=True)
    db_name = models.CharField(max_length=100)
    user_name = models.CharField(max_length=200)
    password = models.CharField(max_length=50)
    host_name = models.CharField(max_length=200)
    port = models.CharField(max_length=4)

    '''def __unicode__(self):
        return self.db_name
    '''
