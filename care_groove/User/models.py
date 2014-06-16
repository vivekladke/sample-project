from django_extensions.db.fields import UUIDField
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin)
from django.utils import timezone
from django.db import models


# Model for EmailUserManager:
class EmailUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        """
        Creates and saves an EmailUser with the given email and password.
        """
        now = timezone.now()
        if not email:
            raise ValueError('The given email must be set')
        email = EmailUserManager.normalize_email(email)
        user = self.model(email=email, is_staff=False, is_active=True,
                          is_superuser=False, last_login=now,
                          date_joined=now, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Creates and saves a superuser with the given email and password.
        """
        user = self.create_user(email, password, **extra_fields)
        user.is_staff = True
        user.is_active = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


# Model for CareGrooveUser:
class CareGrooveUser(AbstractBaseUser, PermissionsMixin):
    class Meta:
        verbose_name = u'Customer'
        verbose_name_plural = u'Customers'

    id = UUIDField(version=4, primary_key=True)
    email = models.EmailField(max_length=254, unique=True,
                              verbose_name=_("Email"))
    name = models.CharField(max_length=30, verbose_name=_("Full Name"))
    is_staff = models.BooleanField(
        default=False,
        help_text=_('Designates whether the user'
                    ' can log into this admin site.'),
        verbose_name=_("Is Staff?"))
    is_active = models.BooleanField(
        default=True,
        help_text=_('Designates whether this user should be treated as'
                    ' active. Unselect this instead of deleting accounts.'),
        verbose_name=_("Is Active?"))
    date_joined = models.DateTimeField(
        default=timezone.now(),
        verbose_name=_("Date Joined"))
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', ]
    objects = EmailUserManager()

    def get_full_name(self):
        return self.name

    def get_short_name(self):
        return self.name.split(" ")[0] if self.name else None
