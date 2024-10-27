# ==============================================================================
# Imports
# ==============================================================================

from netbox.forms import NetBoxModelForm

from django import forms

# import for comment fields, import dynamic choice fields
from utilities.forms.fields import (
    CommentField,
    DynamicModelChoiceField,
    DynamicModelMultipleChoiceField,
)

# ==============================================================================
# Special Model Imports
# ==============================================================================

from .models import (
    Image,
    GoldenImage,
    ImageDistributionServer,
    SettingsDeviceType,
)

from dcim.models import (
    DeviceRole,
    DeviceType,
    Location,
    Platform,
    Region,
    Site,
    SiteGroup,
)

from ipam.models import IPAddress

# ==============================================================================
# Global Variables
# ==============================================================================

# ==============================================================================
# Forms
# ==============================================================================


class ImageForm(NetBoxModelForm):

    image = forms.FileField(
        required=True,
        label="Image",
        help_text="Image File, with .bin extension",
    )

    md5sum = forms.CharField(
        required=True,
        label="MD5 Checksum",
        help_text="Expected MD5 Checksum, ex: 0f58a02f3d3f1e1be8f509d2e5b58fb8",
    )

    version = forms.CharField(
        required=True,
        label="Version",
        help_text="Verbose Software Version, ex: 17.9.3",
    )

    comments = CommentField()

    class Meta:
        model = Image
        fields = (
            "image",
            "md5sum",
            "version",
            "description",
            "comments",
            "tags",
        )


# ==============================================================================


class GoldenImageForm(NetBoxModelForm):

    image = DynamicModelChoiceField(
        queryset=Image.objects.all(),
        label="Image",
        help_text="Chose software image which you want to select as golden image",
        required=True,
    )

    regions = DynamicModelMultipleChoiceField(
        label="Regions", queryset=Region.objects.all(), required=False
    )

    site_groups = DynamicModelMultipleChoiceField(
        label="Site groups", queryset=SiteGroup.objects.all(), required=False
    )

    sites = DynamicModelMultipleChoiceField(
        label="Sites", queryset=Site.objects.all(), required=False
    )

    locations = DynamicModelMultipleChoiceField(
        label="Locations", queryset=Location.objects.all(), required=False
    )

    device_types = DynamicModelMultipleChoiceField(
        label="Device types", queryset=DeviceType.objects.all(), required=False
    )

    roles = DynamicModelMultipleChoiceField(
        label="Roles", queryset=DeviceRole.objects.all(), required=False
    )

    platforms = DynamicModelMultipleChoiceField(
        label="Platforms", queryset=Platform.objects.all(), required=False
    )

    comments = CommentField()

    class Meta:
        model = GoldenImage
        fields = (
            "name",
            "image",
            "description",
            "regions",
            "site_groups",
            "sites",
            "locations",
            "device_types",
            "roles",
            "platforms",
            "comments",
        )


# ==============================================================================


class ImageDistributionServerForm(NetBoxModelForm):

    ip = DynamicModelChoiceField(
        queryset=IPAddress.objects.all(),
        label="IP",
        help_text="Chose ip address of image distribution server",
        required=True,
    )

    comments = CommentField()

    class Meta:
        model = ImageDistributionServer
        fields = (
            "ip",
            "name",
            "description",
            "download_method",
            "custom_port",
            "comments",
        )


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
