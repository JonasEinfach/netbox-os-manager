# ==============================================================================
# Imports
# ==============================================================================

from netbox.models import NetBoxModel
from django.db import models
from django.urls import reverse

from netbox.models.features import JobsMixin

from netbox_os_manager.choices.imagetask import *

# Time
import datetime
from django.utils import timezone

__all__ = ["ImageUploadTask"]

# ==============================================================================
# Global Variables
# ==============================================================================

# ==============================================================================
# Model
# ==============================================================================


class ImageTask(models.Model):

    device = models.ForeignKey(
        verbose_name="device",
        to="dcim.Device",
        on_delete=models.SET_NULL,
        null=True,
    )

    image = models.ForeignKey(
        verbose_name="image", to="Image", on_delete=models.SET_NULL, null=True
    )

    message = models.CharField(
        verbose_name="message",
        max_length=512,
        blank=True,
    )

    scheduled_time = models.DateTimeField(
        verbose_name="Scheduled time", null=True, blank=True
    )

    start_time = models.DateTimeField(verbose_name="Start time", null=True, blank=True)

    end_time = models.DateTimeField(verbose_name="End time", null=True, blank=True)

    max_execution_time_minutes = models.PositiveIntegerField(
        verbose_name="Maximal execution time in minutes", null=True, blank=True
    )

    execution_time = models.TimeField(
        verbose_name="execution time", null=True, blank=True
    )

    class Meta:
        abstract = True


# ==============================================================================


class TaskLog(NetBoxModel):
    task = models.ForeignKey(
        verbose_name="task",
        to="ImageTask",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name="logs",
    )

    subtask_name = models.CharField(
        verbose_name="subtask name", max_length=500, blank=True
    )

    subtask_status = models.CharField(
        verbose_name="subtask status",
        max_length=255,
        choices=ImageTaskLogSubStatusChoices,
        default=ImageTaskLogSubStatusChoices.STATUS_UNKNOWN,
    )

    log_level = models.CharField(
        verbose_name="log level",
        max_length=255,
        choices=ImageTaskLogLevelChoices,
        default=ImageTaskLogLevelChoices.LOG_LEVEL_UNKOWN,
    )

    timestamp = models.DateTimeField(
        verbose_name="timestamp",
        null=True,
    )

    message = models.TextField(verbose_name="message", blank=True, null=True)

    class Meta:
        verbose_name = "Task Log"
        verbose_name_plural = "Task Logs"

    def get_absolute_url(self) -> str:
        return reverse(
            "plugins:netbox_os_manager:tasklog",
            args=[self.pk],
        )

    def __str__(self):
        return f"{self.task}"

    def save(self, *args, **kwargs) -> None:
        # Set Log Timestamp
        self.timestamp: datetime = timezone.now()
        # Save Log
        super().save(*args, **kwargs)


# ==============================================================================


class ImageUploadTask(JobsMixin, ImageTask, NetBoxModel):

    clean_up_inactive_image_files = models.BooleanField(
        verbose_name="Clean up inactive image files before upload.",
        default=True,
    )

    class Meta:
        ordering = ["device", "image"]
        verbose_name = "image upload task"
        verbose_name_plural = "image upload tasks"

    def __str__(self):
        return "Upload %s to %s" % (self.image, self.device)

    def get_absolute_url(self):
        return reverse("plugins:netbox_os_manager:imageuploadtask", args=[self.pk])

    def execute_job(self):
        print("execute job")
        print(self.device)
        print(self.image)
