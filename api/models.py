from django.db import models
from datetime import datetime

# Create your models here.
class Todolist(models.Model):
    title = models.CharField(max_length=20)
    description  = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)
