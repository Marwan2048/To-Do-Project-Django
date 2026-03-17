from django.db import models


class Task(models.Model):
    task = models.CharField(max_length=100, blank=False)  
    details = models.TextField(max_length=250, blank=True, null=True)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.task
