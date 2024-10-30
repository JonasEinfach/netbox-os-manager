# ==============================================================================
# Imports
# ==============================================================================


from rest_framework import serializers

from netbox.api.serializers import NetBoxModelSerializer
from netbox.api.serializers import WritableNestedSerializer


# ==============================================================================
# Special Model Imports
# ==============================================================================


from ..models import (
    Image,
)

# from dcim.api.serializers import (
#     NestedDeviceTypeSerializer,
#     NestedDeviceSerializer,
#     NestedSiteSerializer,
# )


# ==============================================================================
# Nested Serializer
# ==============================================================================


class NestedImageSerializer(WritableNestedSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name="plugins-api:netbox_os_manager-api:image-detail"
    )

    class Meta:
        model = Image
        fields = ("id", "url", "display", "image", "version")


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
