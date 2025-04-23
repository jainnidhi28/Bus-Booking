from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DefaultUserAdmin
from core.models import User

@admin.register(User)
class UserAdmin(DefaultUserAdmin):
    list_display = (
        "id",
        "uuid",
        "email",
        "first_name",
        "last_name",
        "phone_number",
        "created",
        "modified",
    )
    search_fields = ("id", "email", "first_name","phone_number", "last_name")
    list_filter = ("created", "modified")
    readonly_fields = ("id", "uuid", "created", "modified")
    
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'username',
                'password1',
                'password2',
                'email',
                'phone_number',
                'first_name',
                'last_name',
            ),
        }),
    )
