# ==============================================================================
# Imports
# ==============================================================================

from netbox.models import NetBoxModel
from django.db import models
from django.urls import reverse

# Custom stuff
from django.core.validators import MaxValueValidator, MinValueValidator

from netbox_os_manager.choices.imagedistributionserver import *

__all__ = ["ImageDistributionServer"]

# ==============================================================================
# Global Variables
# ==============================================================================


class ImageDistributionServer(NetBoxModel):
    name = models.CharField(verbose_name="name", max_length=100, unique=True)

    ip = models.ForeignKey(
        verbose_name="Image distribution server ip",
        to="ipam.IPAddress",
        on_delete=models.PROTECT,
        blank=True,
        null=True,
        related_name="+",
    )

    description = models.CharField(
        verbose_name="Description", max_length=200, blank=True
    )

    comments = models.TextField(
        blank=True,
    )

    download_method = models.CharField(
        verbose_name="Download method",
        max_length=255,
        choices=ImageDistributionServerDownloadMethodChoices(),
        default=ImageDistributionServerDownloadMethodChoices.DOWNLOAD_METHOD_HTTP,
    )

    custom_port = models.PositiveSmallIntegerField(
        blank=True,
        null=True,
        verbose_name="Custom port",
        validators=[MinValueValidator(1), MaxValueValidator(65535)],
    )

    class Meta:
        ordering = ["name", "ip"]
        verbose_name = "image distribution server"
        verbose_name_plural = "image distribution servers"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse(
            "plugins:netbox_os_manager:imagedistributionserver", args=[self.pk]
        )

    def get_download_method_color(self):
        return ImageDistributionServerDownloadMethodChoices.colors.get(
            self.download_method
        )
