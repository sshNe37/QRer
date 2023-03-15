from django.contrib import admin

from .models import Contact
from django.contrib.auth.models import AbstractUser

#admin.site.register(Contact)

# Register your models here.


from import_export import resources
from import_export.admin import ImportExportMixin
from import_export.admin import ImportExportModelAdmin



class UserResource(resources.ModelResource):
    class Meta:
        model = Contact


@admin.register(Contact)
class UserAdmin(ImportExportMixin, admin.ModelAdmin):
    resource_class = UserResource

from django.contrib.auth import get_user_model
from .models import CustomUser



from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _


CustomUser = get_user_model()

class CustomUserResource(resources.ModelResource):
    class Meta:
        model = CustomUser

class CustomUserAdmin(UserAdmin, ImportExportModelAdmin):
    fieldsets = (
        (None, {"fields": ("username", "password", "studentname")}),
        (_("Personal info"), {"fields": ("email",)}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("username", "password1", "password2", "studentname"),
            },
        ),
    )
    list_display = ("username", "studentname", "is_staff")
    list_filter = ("is_staff", "is_superuser", "is_active", "groups")
    search_fields = ("username", "email")
    ordering = ("username",)

    resource_class = CustomUserResource

#CustomUser = get_user_model()
admin.site.register(CustomUser, CustomUserAdmin)


class CustomResource(resources.ModelResource):
    class Meta:
        model = CustomUser
'''
@admin.register(CustomUser, CustomUserAdmin)
class CustomUserAdmin(ImportExportMixin, admin.ModelAdmin):
    resource_class = CustomResource


class UserResource(resources.ModelResource):
    class Meta:
        model = CustomUser


@admin.register(CustomUser)
class UserAdmin(ImportExportMixin, admin.ModelAdmin):
    resource_class = UserResource
'''