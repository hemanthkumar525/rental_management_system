from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User, Group

admin.site.unregister(User)

class PropertyOwnerAdmin(UserAdmin):
    def get_queryset(self, request):
        """Filter to show only 'property_owner' users."""
        qs = super().get_queryset(request)
        return qs.filter(groups__name="property_owner")

# Register a new admin section for 'property_owner' users
admin.site.register(User, PropertyOwnerAdmin)
