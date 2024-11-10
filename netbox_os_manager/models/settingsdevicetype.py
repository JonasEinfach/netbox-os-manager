# ==============================================================================
# Imports
# ==============================================================================

from netbox.models import NetBoxModel
from django.db import models
from django.urls import reverse

from netbox_os_manager.choices.settingsdevicetype import *

__all__ = ["SettingsDeviceType"]

# ==============================================================================
# Global Variables
# ==============================================================================


class SettingsDeviceType(NetBoxModel):
    device_type = models.OneToOneField(
        to="dcim.DeviceType", on_delete=models.CASCADE, related_name="+", blank=True
    )

    device_remote_filesystem = models.CharField(
        verbose_name="Device remote filesystem",
        help_text="Chose the type of the file system from the device.",
        max_length=255,
        choices=SettingsDeviceFilesystemChoices,
        default=SettingsDeviceFilesystemChoices.FILESYSTEM_BOOTFLASH,
    )

    device_upgrade_mode = models.CharField(
        verbose_name="Device upgrade mode",
        help_text="Chose the upgrade mode of the device.",
        max_length=255,
        choices=SettingsDeviceUpgradeModeChoices,
        default=SettingsDeviceUpgradeModeChoices.UPGRADE_INSTALL_MODE,
    )

    max_attempts_after_reload = models.PositiveSmallIntegerField(
        verbose_name="Max check attempts",
        help_text="Maximum number of attempts to wait until the device is reachable again.",
        default=15,
    )

    seconds_between_attemps_after_reload = models.PositiveSmallIntegerField(
        verbose_name="Wait time",
        help_text="Seconds to wait between the attempts to check if the device is reachable again.",
        default=60,
    )

    minutes_image_add_timeout = models.PositiveSmallIntegerField(
        verbose_name="Image add timeout",
        help_text="Timeout in minutes to wait until the device has successfully added the image.",
        default=10,
    )

    minutes_image_activation_timeout = models.PositiveSmallIntegerField(
        verbose_name="Image activation timeout",
        help_text="Timeout in minutes to wait until the device has successfully activated the image.",
        default=20,
    )

    version_cli_show_command = models.CharField(
        verbose_name="Version cli show command",
        help_text="Enter the cli show command to get the actual version of the device.",
        max_length=255,
        default="show version",
    )

    version_regex_search = models.CharField(
        verbose_name="Regex to get the version",
        help_text="Regular expression to get the version from the version show command.",
        max_length=255,
        default="(?:Version|System version)\s+(\d+\.\d+\.\d+\.\d+)",
    )

    version_regex_group_index = models.PositiveSmallIntegerField(
        verbose_name="Regex capture group index",
        help_text="Index to get from the regex capture group.",
        default=1,
    )

    comments = models.TextField(
        blank=True,
    )

    class Meta:
        ordering = ["device_type", "device_remote_filesystem"]
        verbose_name = "settings device type"
        verbose_name_plural = "settings device types"

    def __str__(self):
        return str(self.device_type.model)

    def get_absolute_url(self):
        return reverse("plugins:netbox_os_manager:settingsdevicetype", args=[self.pk])

    def get_device_remote_filesystem_color(self):
        return SettingsDeviceFilesystemChoices.colors.get(self.device_remote_filesystem)

    def get_device_upgrade_mode_color(self):
        return SettingsDeviceUpgradeModeChoices.colors.get(self.device_upgrade_mode)
