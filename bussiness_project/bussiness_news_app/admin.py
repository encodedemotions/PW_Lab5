from django.contrib import admin
from .models import User


class UserModelAdminDisplay(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name', 'email', )


admin.site.register(User, UserModelAdminDisplay)