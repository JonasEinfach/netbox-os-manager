# ==============================================================================
# Imports
# ==============================================================================

from netbox.models import NetBoxModel
from django.db import models
from django.urls import reverse

# Custom stuff
from django.core.validators import FileExtensionValidator
import hashlib
from pathlib import Path

from netbox_os_manager.choices.image import *

__all__ = ["Image"]

# ==============================================================================
# Global Variables
# ==============================================================================


ImageFolder = "test"


# ==============================================================================
# Model
# ==============================================================================


class Image(NetBoxModel):
    image = models.FileField(
        verbose_name="image",
        upload_to=f"{ImageFolder}/",
        validators=[FileExtensionValidator(allowed_extensions=["bin"])],
        null=True,
        blank=True,
    )

    # automatically set
    filename = models.CharField(
        verbose_name="filename",
        max_length=256,
        blank=True,
    )

    md5sum = models.CharField(
        verbose_name="md5sum",
        max_length=36,
        blank=True,
    )

    # automatically set
    md5sum_calculated = models.CharField(
        verbose_name="md5sum calculated",
        max_length=36,
        blank=True,
    )

    version = models.CharField(
        verbose_name="version",
        max_length=32,
        blank=True,
    )

    description = models.CharField(
        verbose_name="description", max_length=500, blank=True
    )

    comments = models.TextField(
        blank=True,
    )

    # automatically set
    status = models.CharField(
        verbose_name="status",
        max_length=255,
        choices=ImageStatusChoices(),
        default=ImageStatusChoices.IMAGE_STATUS_UNKOWN,
    )

    class Meta:
        ordering = ["filename", "version"]
        verbose_name = "image"
        verbose_name_plural = "images"

    def __str__(self):
        return self.filename

    def get_absolute_url(self):
        return reverse("plugins:netbox_os_manager:image", args=[self.pk])

    def get_status_color(self):
        return ImageStatusChoices.colors.get(self.status)

    def image_exists(self) -> bool:
        return bool(self.image.name)

    # Save method for image file
    def save(self, *args, **kwargs) -> None:
        if not self.image_exists:
            self.filename = ""
            self.md5sum_calculated = ""
            self.md5sum = ""
            super().save(*args, **kwargs)
            return

        # Get Filename from image
        self.filename: str = self.image.name.rsplit("/", 1)[-1]

        # Calculate md5
        md5 = hashlib.md5()
        for chunk in self.image.chunks():
            md5.update(chunk)
        self.md5sum_calculated = md5.hexdigest()

        # Check if md5 match and enable / disable image
        if self.md5sum_calculated == self.md5sum:
            self.status = ImageStatusChoices.IMAGE_STATUS_ACTIVE
        else:
            self.status = ImageStatusChoices.IMAGE_STATUS_ERROR_MD5_MISMATCH

        super().save(*args, **kwargs)
