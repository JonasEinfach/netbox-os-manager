# ==============================================================================
# Imports
# ==============================================================================

from netbox.models import NetBoxModel
from django.db import models
from django.urls import reverse

__all__ = ["GoldenImage"]

# ==============================================================================
# Global Variables
# ==============================================================================


class GoldenImage(NetBoxModel):

    name = models.CharField(verbose_name="name", max_length=100, unique=True)

    image = models.ForeignKey(
        verbose_name="image",
        to="Image",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name="+",
    )

    weight = models.PositiveSmallIntegerField(verbose_name="weight", default=1000)

    description = models.CharField(
        verbose_name="description", max_length=200, blank=True
    )

    comments = models.TextField(
        blank=True,
    )

    regions = models.ManyToManyField(to="dcim.Region", related_name="+", blank=True)

    site_groups = models.ManyToManyField(
        to="dcim.SiteGroup", related_name="+", blank=True
    )

    sites = models.ManyToManyField(to="dcim.Site", related_name="+", blank=True)

    locations = models.ManyToManyField(to="dcim.Location", related_name="+", blank=True)

    device_types = models.ManyToManyField(
        to="dcim.DeviceType", related_name="+", blank=True
    )

    roles = models.ManyToManyField(to="dcim.DeviceRole", related_name="+", blank=True)

    platforms = models.ManyToManyField(to="dcim.Platform", related_name="+", blank=True)

    class Meta:
        ordering = ["name", "image"]
        verbose_name = "golden image"
        verbose_name_plural = "golden images"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("plugins:netbox_os_manager:goldenimage", args=[self.pk])
