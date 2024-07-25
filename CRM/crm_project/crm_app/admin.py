from django.contrib import admin
from .models import Organization, Contact, Deal

@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'phone', 'email', 'date_registered')
    search_fields = ('name', 'address', 'phone', 'email')

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'organization', 'date_registered')
    search_fields = ('name', 'email', 'phone', 'organization__name')

@admin.register(Deal)
class DealAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'amount', 'organization', 'contact', 'date_created')
    search_fields = ('name', 'description', 'amount', 'organization__name', 'contact__name')
