from django.urls import path
from .views import employee_page


urlpatterns = [
    path('', employee_page, name='employee_page'),
]