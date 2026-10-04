from django.shortcuts import render
from rest_framework import viewsets

from .models import ResourceAllocation
from .serializers import ResourceAllocationSerializer


class ResourceAllocationViewSet(viewsets.ModelViewSet):

    queryset = ResourceAllocation.objects.select_related(
        'employee',
        'project'
    ).all()

    serializer_class = ResourceAllocationSerializer


def resource_page(request):

    return render(
        request,
        'resources.html'
    )

from django.shortcuts import render


def dashboard_page(request):
    return render(request, 'dashboard.html')
    
