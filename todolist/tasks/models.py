from django.db import models
from django.utils.timezone import now


class Tag(models.Model):
    name = models.CharField(unique=True, max_length=255)

    def __str__(self):
        return f"{self.name}"


class Todo(models.Model):
    content = models.TextField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(blank=True, null=True)
    is_complete = models.BooleanField()
    tag = models.ManyToManyField(Tag, related_name="tasks")

    def __str__(self):
        return f"{self.content} <--> {self.is_complete} <--> {self.tag}"
