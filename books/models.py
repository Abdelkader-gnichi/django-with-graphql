from django.db import models
import uuid
from django.utils import timezone
# Create your models here.

class BaseModel(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True

class Book(BaseModel):

    name = models.CharField(max_length=100)
    excerpt = models.TextField()

    def __str__(self):
        return f'{self.name}'