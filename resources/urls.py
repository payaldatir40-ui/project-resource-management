from django.urls import path
from .views import resource_page


urlpatterns = [
    path(
        '',
        resource_page,
        name='resource_page'
    ),
]