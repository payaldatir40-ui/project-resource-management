from rest_framework import serializers
from .models import Project


class ProjectSerializer(serializers.ModelSerializer):

    client_name = serializers.CharField(
        source='client.company_name',
        read_only=True
    )

    class Meta:
        model = Project
        fields = [
            'id',
            'project_code',
            'project_name',
            'client',
            'client_name',
            'start_date',
            'end_date',
            'budget',
            'status',
        ]