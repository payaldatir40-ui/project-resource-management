from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from employees.views import EmployeeViewSet
from clients.views import ClientViewSet
from projects.views import ProjectViewSet
from resources.views import ResourceAllocationViewSet
from resources.views import dashboard_page

router = DefaultRouter()

router.register(
    r'employees',
    EmployeeViewSet
)

router.register(
    r'clients',
    ClientViewSet
)

router.register(
    r'projects',
    ProjectViewSet
)

router.register(
    r'resources',
    ResourceAllocationViewSet
)


urlpatterns = [

    path(
        'admin/',
        admin.site.urls
    ),

    # REST API
    path(
        'api/',
        include(router.urls)
    ),

    # Frontend
    path(
        'employees/',
        include('employees.urls')
    ),

    path(
    'clients/',
    include('clients.urls')
     ),

     path(
    'projects/',
    include('projects.urls')
),

path(
    'resources/',
    include('resources.urls')
),

path(
    '',
    dashboard_page,
    name='dashboard'
),
]