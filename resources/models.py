from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

from employees.models import Employee
from projects.models import Project


class ResourceAllocation(models.Model):

    ROLE_CHOICES = [
        ('Developer', 'Developer'),
        ('Data Analyst', 'Data Analyst'),
        ('Data Engineer', 'Data Engineer'),
        ('BI Developer', 'BI Developer'),
        ('Tech Lead', 'Tech Lead'),
        ('Business Analyst', 'Business Analyst'),
        ('QA Engineer', 'QA Engineer'),
        ('Technical Consultant', 'Technical Consultant'),
        ('Project Manager', 'Project Manager'),
    ]

    employee = models.ForeignKey(
        Employee,
        on_delete=models.CASCADE,
        related_name='resource_allocations'
    )

    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name='resource_allocations'
    )

    role = models.CharField(
        max_length=100,
        choices=ROLE_CHOICES
    )

    allocation_percentage = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        validators=[
            MinValueValidator(0),
            MaxValueValidator(100)
        ]
    )

    allocation_start_date = models.DateField()

    allocation_end_date = models.DateField()

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['employee', 'project'],
                name='unique_employee_project'
            )
        ]

    def __str__(self):
        return (
            f"{self.employee} - "
            f"{self.project} - "
            f"{self.allocation_percentage}%"
        )
