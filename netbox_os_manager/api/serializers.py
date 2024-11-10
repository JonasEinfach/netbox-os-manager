# ==============================================================================
# Imports
# ==============================================================================


from rest_framework import serializers

from netbox.api.serializers import NetBoxModelSerializer
from netbox.api.serializers import WritableNestedSerializer


# ==============================================================================
# Special Model Imports
# ==============================================================================


from netbox_os_manager.models import *
from dcim.models import (
    DeviceRole,
    DeviceType,
    Location,
    Platform,
    Region,
    Site,
    SiteGroup,
)

# using special serializers
from dcim.api.serializers import (
    SiteGroupSerializer,
    SiteSerializer,
    LocationSerializer,
    RegionSerializer,
    PlatformSerializer,
    DeviceRoleSerializer,
    DeviceTypeSerializer,
)

from ipam.api.serializers import IPAddressSerializer

from netbox.api.serializers import ValidatedModelSerializer
from netbox.api.fields import SerializedPKRelatedField

# ==============================================================================
# Serializer
# ==============================================================================


class ImageSerializer(NetBoxModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name="plugins-api:netbox_os_manager-api:image-detail"
    )

    class Meta:
        model = Image
        fields = (
            "id",
            "url",
            "display",
            "image",
            "status",
            "md5sum",
            "md5sum_calculated",
            "version",
            "filename",
            "description",
            "comments",
            "tags",
            "custom_fields",
            "created",
            "last_updated",
        )
        brief_fields = (
            "id",
            "url",
            "display",
            "status",
            "filename",
            "version",
            "description",
            "status",
        )


# ==============================================================================


class GoldenImageSerializer(ValidatedModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name="plugins-api:netbox_os_manager-api:goldenimage-detail"
    )

    image = ImageSerializer(nested=True)

    regions = SerializedPKRelatedField(
        queryset=Region.objects.all(),
        serializer=RegionSerializer,
        nested=True,
        required=False,
        many=True,
    )

    site_groups = SerializedPKRelatedField(
        queryset=SiteGroup.objects.all(),
        serializer=SiteGroupSerializer,
        nested=True,
        required=False,
        many=True,
    )

    sites = SerializedPKRelatedField(
        queryset=Site.objects.all(),
        serializer=SiteSerializer,
        nested=True,
        required=False,
        many=True,
    )

    locations = SerializedPKRelatedField(
        queryset=Location.objects.all(),
        serializer=LocationSerializer,
        nested=True,
        required=False,
        many=True,
    )

    device_types = SerializedPKRelatedField(
        queryset=DeviceType.objects.all(),
        serializer=DeviceTypeSerializer,
        nested=True,
        required=False,
        many=True,
    )

    roles = SerializedPKRelatedField(
        queryset=DeviceRole.objects.all(),
        serializer=DeviceRoleSerializer,
        nested=True,
        required=False,
        many=True,
    )

    platforms = SerializedPKRelatedField(
        queryset=Platform.objects.all(),
        serializer=PlatformSerializer,
        nested=True,
        required=False,
        many=True,
    )

    class Meta:
        model = GoldenImage
        fields = (
            "id",
            "url",
            "display",
            "name",
            "image",
            "weight",
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
        brief_fields = (
            "id",
            "url",
            "display",
            "name",
            "image",
            "weight",
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


class ImageDistributionServerSerializer(ValidatedModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name="plugins-api:netbox_os_manager-api:imagedistributionserver-detail"
    )

    ip = IPAddressSerializer(nested=True)

    class Meta:
        model = ImageDistributionServer
        fields = (
            "id",
            "url",
            "display",
            "name",
            "ip",
            "description",
            "comments",
            "download_method",
            "custom_port",
        )
        brief_fields = (
            "id",
            "url",
            "display",
            "name",
            "ip",
            "description",
            "download_method",
            "custom_port",
        )


# ==============================================================================


class SettingsDeviceTypeSerializer(ValidatedModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name="plugins-api:netbox_os_manager-api:settingsdevicetype-detail"
    )

    device_type = DeviceTypeSerializer(nested=True)

    class Meta:
        model = SettingsDeviceType
        fields = (
            "id",
            "url",
            "display",
            "device_type",
            "device_remote_filesystem",
            "device_upgrade_mode",
            "max_attempts_after_reload",
            "seconds_between_attemps_after_reload",
            "minutes_image_add_timeout",
            "minutes_image_activation_timeout",
            "version_cli_show_command",
            "version_regex_search",
            "version_regex_group_index",
            "comments",
        )
        brief_fields = (
            "id",
            "url",
            "display",
            "device_type",
            "device_remote_filesystem",
            "device_upgrade_mode",
            "comments",
        )


# ==============================================================================
