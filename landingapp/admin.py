from django.contrib import admin

from landingapp.models import User

# Register your models here.

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')
    ordering = ('name', 'email',)
    list_per_page = 20
    search_fields = ('name', 'email')
    actions = ('mark_as_delete', 'mark_as_active', 'mark_as_superuser', 'mark_as_user')
    list_display_links = ('name', 'email')