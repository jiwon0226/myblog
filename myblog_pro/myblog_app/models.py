from django.db import models
from django.utils import timezone
# Create your models here.
class Board(models.Model):
    title = models.CharField(max_length=30)
    authon = models.CharField(max_length=20)
    content = models.TextField()
    create_at = models.DateTimeField(default=timezone.now)
