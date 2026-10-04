from rest_framework import serializers
from .models import ResourceAllocation


class ResourceAllocationSerializer(serializers.ModelSerializer):

    employee_name = serializers.SerializerMethodField()
    project_name = serializers.SerializerMethodField()

    class Meta:
        model = ResourceAllocation

        fields = [
            'id',
            'employee',
            'employee_name',
            'project',
            'project_name',
            'role',
            'allocation_percentage',
            'allocation_start_date',
            'allocation_end_date',
        ]

    def get_employee_name(self, obj):
        return f"{obj.employee.first_name} {obj.employee.last_name}"

    def get_project_name(self, obj):
        return obj.project.project_name