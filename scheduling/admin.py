from django.contrib import admin
from .models import Profile, Slot, Schedule

# admin.site.register(Profile)
admin.site.register(Slot)
admin.site.register(Schedule)

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone_number', 'bio')  # Add other fields as needed
    search_fields = ['user__username', 'phone_number']
    list_filter = ('user__is_staff', 'user__is_superuser')

    # If you have custom form, ensure that 'phone_number' is included in fields
    fieldsets = (
        (None, {'fields': ('user', 'bio', 'phone_number')}),
    )

admin.site.register(Profile, ProfileAdmin)
