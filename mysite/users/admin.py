from django.contrib import admin

from users.models import test_tab, UserLoginProfile

admin.site.register(test_tab)
admin.site.register(UserLoginProfile)
