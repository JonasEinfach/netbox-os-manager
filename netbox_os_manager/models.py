# ==============================================================================
# Imports
# ==============================================================================

from django.contrib.postgres.fields import ArrayField
from django.db import models
from netbox.models import NetBoxModel

# choice set
from utilities.choices import ChoiceSet

# using for get absolute url
from django.urls import reverse

# ==============================================================================
# Special Model Imports
# ==============================================================================

# For file extension validation
from django.core.validators import FileExtensionValidator

# For md5 hashing
import hashlib

# For deletion of images
from pathlib import Path

# Time for tasklog
import datetime
from django.utils import timezone

# For Integer Validator
from django.core.validators import MaxValueValidator, MinValueValidator

# ==============================================================================
# Global Variables
# ==============================================================================

ImageFolder = "test"

# ==============================================================================
# Custom ChoiceSet
# ==============================================================================

# Choices for Image Status
# Choices not changeable by admin via configuration.py


class ImageStatusChoices(ChoiceSet):
    IMAGE_STATUS_UNKOWN = "unkown"
    IMAGE_STATUS_ACTIVE = "active"
    IMAGE_STATUS_ERROR_MD5_MISMATCH = "error md5 mismatch"

    CHOICES = [
        (IMAGE_STATUS_UNKOWN, "Unkown", "black"),
        (IMAGE_STATUS_ACTIVE, "Active", "green"),
        (IMAGE_STATUS_ERROR_MD5_MISMATCH, "Error-MD5-Mismatch", "red"),
    ]


# ==============================================================================

# Choices for Image Distribution Server download method
# Choices not changeable by admin via configuration.py


class ImageDistributionServerDownloadMethodChoices(ChoiceSet):
    DOWNLOAD_METHOD_HTTP = "http"
    DOWNLOAD_METHOD_FTP = "ftp"

    CHOICES = [
        (DOWNLOAD_METHOD_HTTP, "HTTP", "yellow"),
        (DOWNLOAD_METHOD_FTP, "FTP", "yellow"),
    ]


# ==============================================================================

# Choices for Task Log
# Choices not changeable by admin via configuration.py


class TaskLogSubStatusChoices(ChoiceSet):
    STATUS_UNKNOWN = "unknown"
    STATUS_RUNNING = "running"
    STATUS_SUCCEEDED = "succeeded"
    STATUS_WARNING = "warning"
    STATUS_ERROR = "error"
    CHOICES = [
        (STATUS_UNKNOWN, "Unknown", "white"),
        (STATUS_RUNNING, "Running", "pink"),
        (STATUS_SUCCEEDED, "Succeeded", "green"),
        (STATUS_WARNING, "Warning", "orange"),
        (STATUS_ERROR, "Error", "red"),
    ]


# ==============================================================================

# Choices for Task Log Level
# Choices not changeable by admin via configuration.py


class TaskLogLevelChoices(ChoiceSet):
    LOG_LEVEL_UNKOWN = "unkown"
    LOG_LEVEL_INFO = "info"
    LOG_LEVEL_WARNING = "warning"
    LOG_LEVEL_ERROR = "error"
    LOG_LEVEL_DEBUG = "debug"
    CHOICES = [
        (LOG_LEVEL_UNKOWN, "Unknown", "white"),
        (LOG_LEVEL_INFO, "Info", "yellow"),
        (LOG_LEVEL_WARNING, "Warning", "orange"),
        (LOG_LEVEL_ERROR, "Error", "red"),
        (LOG_LEVEL_DEBUG, "Debug", "pink"),
    ]


# ==============================================================================

# Choices for Upgrade Device
# Choices not changeable by admin via configuration.py


class UpgradeDeviceStatusChoices(ChoiceSet):
    STATUS_UNKNOWN = "unkown"
    STATUS_PLANNED = "planned"
    STATUS_IMAGE_UPLOAD_SCHEDULED = "image upload scheduled"
    STATUS_IMAGE_UPLOAD_FAIL = "image upload fail"
    STATUS_IMAGE_UPLOAD_DONE = "image upload done"
    STATUS_IMAGE_ADD_SCHEDULED = "image add scheduled"
    STATUS_IMAGE_ADD_FAIL = "image add fail"
    STATUS_IMAGE_ADD_DONE = "image add done"
    STATUS_IMAGE_ACTIVATION_SCHEDULED = "image activation scheduled"
    STATUS_IMAGE_ACTIVATION_FAIL = "image activation fail"
    STATUS_UPGRADE_DONE = "image upgrade done"

    CHOICES = [
        (STATUS_UNKNOWN, "Unknown", "white"),
        (STATUS_PLANNED, "Planned", "yellow"),
        (STATUS_IMAGE_UPLOAD_SCHEDULED, "Image Upload Scheduled", "pink"),
        (STATUS_IMAGE_UPLOAD_FAIL, "Image Upload Fail", "red"),
        (STATUS_IMAGE_UPLOAD_DONE, "Image Upload Done", "teal"),
        (STATUS_IMAGE_ADD_SCHEDULED, "Image Add Scheduled", "pink"),
        (STATUS_IMAGE_ADD_FAIL, "Image Add Fail", "red"),
        (STATUS_IMAGE_ADD_DONE, "Image Add Done", "teal"),
        (STATUS_IMAGE_ACTIVATION_SCHEDULED, "Image Activation Scheduled", "pink"),
        (STATUS_IMAGE_ACTIVATION_FAIL, "Image Activation Fail", "red"),
        (STATUS_UPGRADE_DONE, "Image Upgrade Done", "green"),
    ]


# ==============================================================================

# Choices for Upgrade Device
# Choices not changeable by admin via configuration.py


class SettingsDeviceFilesystemChoices(ChoiceSet):
    FILESYSTEM_BOOTFLASH = "bootflash:"
    FILESYSTEM_SDFLASH = "sdflash:"

    CHOICES = [
        (FILESYSTEM_BOOTFLASH, "bootflash:", "grey"),
        (FILESYSTEM_SDFLASH, "sdflash:", "grey"),
    ]


# ==============================================================================

# Choices for Upgrade Device
# Choices not changeable by admin via configuration.py


class SettingsDeviceUpgradeMode(ChoiceSet):
    UPGRADE_INSTALL_MODE = "INSTALL_MODE"
    # UPGRADE_BUNDLE_MODE = "BUNDLE_MODE"
    # Bundle mode is still not supported

    CHOICES = [
        (UPGRADE_INSTALL_MODE, "INSTALL_MODE", "grey"),
        # (UPGRADE_BUNDLE_MODE, "BUNDLE_MODE", "grey"),
    ]


# ==============================================================================
# Models
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


# ==============================================================================


# Todo: Implement together with Task/Jobs

# class TaskLog(NetBoxModel):
#     task = models.ForeignKey(
#         verbose_name="task",
#         to="Task",
#         on_delete=models.CASCADE,
#         blank=True,
#         null=True,
#         related_name="logs",
#     )

#     subtask_name = models.CharField(
#         verbose_name="subtask name", max_length=500, blank=True
#     )

#     subtask_status = models.CharField(
#         verbose_name="subtask status",
#         max_length=255,
#         choices=TaskLogSubStatusChoices,
#         default=TaskLogSubStatusChoices.STATUS_UNKNOWN,
#     )

#     log_level = models.CharField(
#         verbose_name="log level",
#         max_length=255,
#         choices=TaskLogLevelChoices,
#         default=TaskLogLevelChoices.LOG_LEVEL_UNKOWN,
#     )

#     timestamp = models.DateTimeField(
#         verbose_name="timestamp",
#         null=True,
#     )

#     message = models.TextField(verbose_name="message", blank=True, null=True)

#     class Meta:
#         verbose_name = "Task Log"
#         verbose_name_plural = "Task Logs"

#     def __str__(self):
#         return f"{self.task}"

#     def save(self, *args, **kwargs) -> None:
#         # Set Log Timestamp
#         self.timestamp: datetime = timezone.now()
#         # Save Log
#         super().save(*args, **kwargs)


# ==============================================================================

# Todo: Implement together with Task/Jobs

# class UpgradeDevice(NetBoxModel):
#     device = models.OneToOneField(
#         verbose_name="Device",
#         to="dcim.Device",
#         on_delete=models.SET_NULL,
#         null=True,
#         related_name="upgrade_device_process",
#     )

#     image = models.ForeignKey(
#         verbose_name="Image", to="Image", on_delete=models.SET_NULL, null=True
#     )

#     status = models.CharField(
#         verbose_name="Status",
#         max_length=255,
#         choices=UpgradeDeviceStatusChoices,
#         default=UpgradeDeviceStatusChoices.STATUS_UNKNOWN,
#     )

#     image_uploaded = models.BooleanField(
#         verbose_name="Image uploaded",
#         default=False,
#     )

#     image_upload_task = models.ForeignKey(
#         verbose_name="Image upload task",
#         to="SWMGTask",
#         on_delete=models.SET_NULL,
#         null=True,
#         related_name="device_upgrade_image_upload_task",
#     )

#     image_added = models.BooleanField(
#         verbose_name="Image added",
#         default=False,
#     )

#     image_add_task = models.ForeignKey(
#         verbose_name="Image add task",
#         to="SWMGTask",
#         on_delete=models.SET_NULL,
#         null=True,
#         related_name="device_upgrade_image_add_task",
#     )

#     image_activated = models.BooleanField(
#         verbose_name="Image activated",
#         default=False,
#     )

#     image_activation_task = models.ForeignKey(
#         verbose_name="Image activation task",
#         to="SWMGTask",
#         on_delete=models.SET_NULL,
#         null=True,
#         related_name="device_upgrade_image_activation_task",
#     )

#     class Meta:
#         verbose_name = "Upgrade Device"
#         verbose_name_plural = "Upgrade Devices"

#     def get_absolute_url(self) -> str:
#         return reverse(
#             "plugins:netbox_mtu_campus_automation:swmgupgradedevice",
#             args=[self.pk],
#         )

#     def __str__(self):
#         return "Upgrade %s to %s" % (self.device.name, self.image.filename)

#     def get_status_color(self):
#         return UpgradeDeviceStatusChoices.colors.get(self.status)

#     def save(self, *args, **kwargs) -> None:
#         if not self.pk:
#             # Initial Upgrade Device Creation
#             self.status = UpgradeDeviceStatusChoices.STATUS_PLANNED
#             super().save(*args, **kwargs)
#         else:
#             super().save(*args, **kwargs)

#     def set_task_image_upload(self, task: Task):
#         if not self.image_upload_task:
#             self.image_upload_task = task
#             self.status = UpgradeDeviceStatusChoices.STATUS_IMAGE_UPLOAD_SCHEDULED
#             super().save()

#     def set_task_image_add(self, task: Task):
#         if self.image_upload_task:
#             self.image_add_task = task
#             self.status = UpgradeDeviceStatusChoices.STATUS_IMAGE_ADD_SCHEDULED
#             super().save()

#     def set_task_image_activation(self, task: Task):
#         if self.image_add_task:
#             self.image_activation_task = task
#             self.status = (
#                 UpgradeDeviceStatusChoices.STATUS_IMAGE_ACTIVATION_SCHEDULED
#             )
#             super().save()


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
        choices=SettingsDeviceUpgradeMode,
        default=SettingsDeviceUpgradeMode.UPGRADE_INSTALL_MODE,
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


# ==============================================================================
