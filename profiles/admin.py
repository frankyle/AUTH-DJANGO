from django.contrib import admin
from .models import Profile

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone_number', 'nationality', 'region', 'age', 'informed_by')
    search_fields = ('user__email', 'phone_number', 'nationality', 'region')
    list_filter = ('nationality', 'region')
    
    # Optional: Customize fields display in the admin detail view
    fieldsets = (
        (None, {
            'fields': ('user', 'phone_number', 'nationality', 'region', 'age', 'image', 'informed_by')
        }),
    )
