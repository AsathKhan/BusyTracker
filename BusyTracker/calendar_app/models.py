from django.db import models

# Create your models here.
class Reminder(models.Model):
    date = models.DateField()
    time = models.TimeField(null=True, blank=True)
    description = models.TextField()
    
    def __str__(self):
        return f"{self.date} - {self.description}"
