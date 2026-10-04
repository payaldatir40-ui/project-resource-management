from django.contrib import admin
from .models import Project


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):

    list_display = (
        'project_code',
        'project_name',
        'client',
        'start_date',
        'end_date',
        'budget',
        'status',
    )

    search_fields = (
        'project_code',
        'project_name',
        'client__company_name',
    )

    list_filter = (
        'status',
    )

    ordering = (
        'project_code',
    )