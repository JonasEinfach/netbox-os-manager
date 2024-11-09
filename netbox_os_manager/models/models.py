# Time for tasklog
# import datetime
# from django.utils import timezone


# ==============================================================================
# Global Variables
# ==============================================================================


# ==============================================================================
# Custom ChoiceSet
# ==============================================================================

# Choices for Image Status
# Choices not changeable by admin via configuration.py


# class ImageStatusChoices(ChoiceSet):
#     IMAGE_STATUS_UNKOWN = "unkown"
#     IMAGE_STATUS_ACTIVE = "active"
#     IMAGE_STATUS_ERROR_MD5_MISMATCH = "error md5 mismatch"

#     CHOICES = [
#         (IMAGE_STATUS_UNKOWN, "Unkown", "black"),
#         (IMAGE_STATUS_ACTIVE, "Active", "green"),
#         (IMAGE_STATUS_ERROR_MD5_MISMATCH, "Error-MD5-Mismatch", "red"),
#     ]


# ==============================================================================

# Choices for Image Distribution Server download method
# Choices not changeable by admin via configuration.py


# class ImageDistributionServerDownloadMethodChoices(ChoiceSet):
#     DOWNLOAD_METHOD_HTTP = "http"
#     DOWNLOAD_METHOD_FTP = "ftp"

#     CHOICES = [
#         (DOWNLOAD_METHOD_HTTP, "HTTP", "teal"),
#         (DOWNLOAD_METHOD_FTP, "FTP", "pink"),
#     ]


# ==============================================================================

# Choices for Task Log
# Choices not changeable by admin via configuration.py


# class TaskLogSubStatusChoices(ChoiceSet):
#     STATUS_UNKNOWN = "unknown"
#     STATUS_RUNNING = "running"
#     STATUS_SUCCEEDED = "succeeded"
#     STATUS_WARNING = "warning"
#     STATUS_ERROR = "error"
#     CHOICES = [
#         (STATUS_UNKNOWN, "Unknown", "white"),
#         (STATUS_RUNNING, "Running", "pink"),
#         (STATUS_SUCCEEDED, "Succeeded", "green"),
#         (STATUS_WARNING, "Warning", "orange"),
#         (STATUS_ERROR, "Error", "red"),
#     ]


# ==============================================================================

# Choices for Task Log Level
# Choices not changeable by admin via configuration.py


# class TaskLogLevelChoices(ChoiceSet):
#     LOG_LEVEL_UNKOWN = "unkown"
#     LOG_LEVEL_INFO = "info"
#     LOG_LEVEL_WARNING = "warning"
#     LOG_LEVEL_ERROR = "error"
#     LOG_LEVEL_DEBUG = "debug"
#     CHOICES = [
#         (LOG_LEVEL_UNKOWN, "Unknown", "white"),
#         (LOG_LEVEL_INFO, "Info", "yellow"),
#         (LOG_LEVEL_WARNING, "Warning", "orange"),
#         (LOG_LEVEL_ERROR, "Error", "red"),
#         (LOG_LEVEL_DEBUG, "Debug", "pink"),
#     ]


# ==============================================================================

# Choices for Upgrade Device
# Choices not changeable by admin via configuration.py


# class UpgradeDeviceStatusChoices(ChoiceSet):
#     STATUS_UNKNOWN = "unkown"
#     STATUS_PLANNED = "planned"
#     STATUS_IMAGE_UPLOAD_SCHEDULED = "image upload scheduled"
#     STATUS_IMAGE_UPLOAD_FAIL = "image upload fail"
#     STATUS_IMAGE_UPLOAD_DONE = "image upload done"
#     STATUS_IMAGE_ADD_SCHEDULED = "image add scheduled"
#     STATUS_IMAGE_ADD_FAIL = "image add fail"
#     STATUS_IMAGE_ADD_DONE = "image add done"
#     STATUS_IMAGE_ACTIVATION_SCHEDULED = "image activation scheduled"
#     STATUS_IMAGE_ACTIVATION_FAIL = "image activation fail"
#     STATUS_UPGRADE_DONE = "image upgrade done"

#     CHOICES = [
#         (STATUS_UNKNOWN, "Unknown", "white"),
#         (STATUS_PLANNED, "Planned", "yellow"),
#         (STATUS_IMAGE_UPLOAD_SCHEDULED, "Image Upload Scheduled", "pink"),
#         (STATUS_IMAGE_UPLOAD_FAIL, "Image Upload Fail", "red"),
#         (STATUS_IMAGE_UPLOAD_DONE, "Image Upload Done", "teal"),
#         (STATUS_IMAGE_ADD_SCHEDULED, "Image Add Scheduled", "pink"),
#         (STATUS_IMAGE_ADD_FAIL, "Image Add Fail", "red"),
#         (STATUS_IMAGE_ADD_DONE, "Image Add Done", "teal"),
#         (STATUS_IMAGE_ACTIVATION_SCHEDULED, "Image Activation Scheduled", "pink"),
#         (STATUS_IMAGE_ACTIVATION_FAIL, "Image Activation Fail", "red"),
#         (STATUS_UPGRADE_DONE, "Image Upgrade Done", "green"),
#     ]


# ==============================================================================
# Models
# ==============================================================================


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
