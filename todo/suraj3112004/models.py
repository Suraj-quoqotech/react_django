from django.db import models

class Todo(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    due_date = models.DateField(null=True, blank=True)
    priority = models.CharField(max_length=20, default="Medium")  # Low / Medium / High
    status = models.CharField(max_length=20, default="Pending")   # Pending / Done

    def __str__(self):
        return self.title
