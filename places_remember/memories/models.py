from django.db import models
from user_profile.models import CustomUser


class Memory(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True, default=None)
    user_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    place = models.CharField(max_length=255, blank=True, null=True, default=None)
    description = models.TextField(blank=True, null=True, default=None)

    class Meta:
        verbose_name = "Memory"
        verbose_name_plural = "Memories"


class MemoryImage(models.Model):
    memory = models.ForeignKey(
        Memory, blank=True, null=True, default=None, on_delete=models.CASCADE
    )
    image = models.ImageField(default="static/media/placeholder.png")
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    class Meta:
        verbose_name = "Image"
        verbose_name_plural = "Images"
