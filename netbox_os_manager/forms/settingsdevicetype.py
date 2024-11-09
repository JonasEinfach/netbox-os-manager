# ==============================================================================
# Imports
# ==============================================================================

from netbox.forms import NetBoxModelForm, NetBoxModelBulkEditForm
from django import forms
from utilities.forms.fields import (
    CommentField,
    DynamicModelChoiceField,
    DynamicModelMultipleChoiceField,
)
from utilities.forms.rendering import FieldSet

# Custom stuff
from dcim.models import DeviceType

from netbox_os_manager.models.settingsdevicetype import *
from netbox_os_manager.choices.settingsdevicetype import *

__all__ = ["SettingsDeviceTypeForm", "SettingsDeviceTypeBulkEditForm"]

# ==============================================================================
# Forms
# ==============================================================================


class SettingsDeviceTypeForm(NetBoxModelForm):

    device_type = DynamicModelChoiceField(
        label=("Device type"), queryset=DeviceType.objects.all(), required=True
    )

    comments = CommentField()

    class Meta:
        model = SettingsDeviceType
        fields = (
            "device_type",
            "device_remote_filesystem",
            "device_upgrade_mode",
            "max_attempts_after_reload",
            "seconds_between_attemps_after_reload",
            "minutes_image_add_timeout",
            "minutes_image_activation_timeout",
        )


# ==============================================================================


class SettingsDeviceTypeBulkEditForm(NetBoxModelBulkEditForm):

    device_remote_filesystem = forms.ChoiceField(
        choices=SettingsDeviceFilesystemChoices, required=False
    )

    device_upgrade_mode = forms.ChoiceField(
        choices=SettingsDeviceUpgradeModeChoices, required=False
    )

    model = SettingsDeviceType
    fieldsets = (
        FieldSet(
            "device_remote_filesystem",
            "device_upgrade_mode",
            "max_attempts_after_reload",
            "seconds_between_attemps_after_reload",
            "minutes_image_add_timeout",
            "minutes_image_activation_timeout",
            name=("Settings"),
        ),
    )
