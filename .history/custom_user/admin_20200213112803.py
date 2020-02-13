from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm

from custom_user.models import CustomUser


class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = CustomUser


class CustomUserAdmin(UserAdmin):
    # form = CustomUserChangeForm

    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': (
                'homepage',
                'display_name',
                'age',
                ''
                )}),
    )


admin.site.register(CustomUser, CustomUserAdmin)
