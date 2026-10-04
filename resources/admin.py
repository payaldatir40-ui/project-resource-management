from django.contrib import admin
from .models import ResourceAllocation


@admin.register(ResourceAllocation)
class ResourceAllocationAdmin(admin.ModelAdmin):

    list_display = (
        'employee',
        'project',
        'role',
        'allocation_percentage',
        'allocation_start_date',
        'allocation_end_date',
    )

    search_fields = (
        'employee__employee_code',
        'employee__first_name',
        'employee__last_name',
        'project__project_code',
        'project__project_name',
    )

    list_filter = (
        'role',
        'project',
    )

    ordering = (
        'project',
        'employee',
    )