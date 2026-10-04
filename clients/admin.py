from django.contrib import admin
from .models import Client


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):

    list_display = (
        'client_code',
        'company_name',
        'contact_person',
        'email',
        'industry',
        'status',
    )

    search_fields = (
        'client_code',
        'company_name',
        'contact_person',
        'email',
    )

    list_filter = (
        'industry',
        'status',
    )