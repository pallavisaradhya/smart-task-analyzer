
# Create your models here.
from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=255)  # Task title
    due_date = models.DateField()             # Task due date
    estimated_hours = models.FloatField()     # Estimated effort in hours
    importance = models.IntegerField()        # Importance scale 1-10
    dependencies = models.ManyToManyField(
        'self', symmetrical=False, blank=True
    )  # Other tasks that this task depends on

    def __str__(self):
     return self.title