from django.db import models
from clients.models import Client


class Project(models.Model):

    STATUS_CHOICES = [
        ('Planned', 'Planned'),
        ('In Progress', 'In Progress'),
        ('Completed', 'Completed'),
        ('On Hold', 'On Hold'),
        ('Cancelled', 'Cancelled'),
    ]

    project_code = models.CharField(
        max_length=20,
        unique=True
    )

    project_name = models.CharField(
        max_length=150
    )

    client = models.ForeignKey(
        Client,
        on_delete=models.CASCADE,
        related_name='projects'
    )

    start_date = models.DateField()

    end_date = models.DateField()

    budget = models.DecimalField(
        max_digits=15,
        decimal_places=2
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='Planned'
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return f"{self.project_code} - {self.project_name}"