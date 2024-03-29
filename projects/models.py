from django.db import models
from django.utils.translation import gettext_lazy as _

class Project(models.Model):
    class Status(models.TextChoices):
        ACTIVE = 'ACT', _('Active')
        COMPLETED = 'COM', _('Completed')
        PAUSED = 'PAU', _('Paused')

    title = models.CharField(max_length=200)
    description = models.TextField()
    tech = models.CharField(max_length=200)
    status = models.CharField(
        max_length=3,
        choices=Status.choices,
        default=Status.ACTIVE,
    )
    image_url = models.URLField(null=True, blank=True)
    project_url = models.URLField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
