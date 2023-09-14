from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import StaffUser, Customer

class StaffUserAdmin(UserAdmin):
    def get_fieldsets(self, request, obj=None):
        if obj is not None and obj.is_superuser:
            # Superuser view
            return (
                (None, {'fields': ('username', 'password')}),
                ('Personal Info', {'fields': ('first_name', 'last_name', 'email')}),
                ('Permissions', {
                    'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
                }),
            )
        else:
            # Staff user view
            return (
                (None, {'fields': ('username', 'password')}),
                ('Personal Info', {'fields': ('first_name', 'last_name', 'email')}),
                ('Permissions', {
                    'fields': ('is_active', 'is_staff', 'groups', 'user_permissions'),
                }),
            )

    def get_readonly_fields(self, request, obj=None):
        if obj is not None and obj.is_superuser:
            # Superuser view
            return ()
        else:
            # Staff user view
            return ('is_superuser', 'user_permissions')

# Register the StaffUser model with the custom admin class
admin.site.register(StaffUser, StaffUserAdmin)

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'email')
    search_fields = ('name', 'email')
    list_filter = ()

# Register the models with the admin site

admin.site.register(Customer, CustomerAdmin)
