from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class StaffUser(AbstractUser):
    # Inheriting from AbstractUser to have standard User fields.

    # Additional fields specific to Staff User can be added here.
    # For example:
    # staff_field = models.CharField(max_length=255)

    def get_assigned_permissions(self):
        # This method retrieves the permissions assigned to the staff user.
        return self.user_permissions.all() | Permission.objects.filter(staffuser__user=self)

    def get_assigned_groups(self):
        # This method retrieves the groups to which the staff user belongs.
        return self.groups.all()

    class Meta:
        permissions = [
            # Define custom permissions here if needed.
            # Example:
            # ("can_do_something", "Can do something"),
        ]

class StaffGroup(Group):
    # You can create a custom StaffGroup model if you need additional fields for staff groups.
    pass


class Customer(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password = models.CharField(blank=False,max_length=90,null=None)

    def __str__(self):
        return self.name
