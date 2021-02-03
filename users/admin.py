from django.contrib.auth.admin import UserAdmin
from django.contrib import admin
from . import models

# Register your models here.


@admin.register(models.User)
class CustomUserAdmin(UserAdmin):
    """CUSTOM USER ADMIN"""

    fieldsets = UserAdmin.fieldsets + (
        (
            "Custom Profile",
            {"fields": ("avatar", "gender", "dob", "language", "currency", "bio")},
        ),
    )

    list_filter = UserAdmin.list_filter + (
        "superhost",
        )

    list_display = (
        "username",
        "first_name",
        "last_name",
        "email",
        "is_active",
        "language",
        "currency",
        "superhost",
        "is_staff",
        "superhost",
    )