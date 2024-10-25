# ==============================================================================
# Imports
# ==============================================================================

import django_tables2 as tables

from netbox.tables import (
    NetBoxTable,
    TemplateColumn,
    ChoiceFieldColumn,
    ContentTypesColumn,
    columns,
)

from netbox.tables.columns import ActionsColumn, ToggleColumn, ColoredLabelColumn
from django_tables2.utils import Accessor

# ==============================================================================
# Special Model Imports
# ==============================================================================

from .models import (
    Image,
    GoldenImage,
    ImageDistributionServer,
    SettingsDeviceType,
)

# using netbox devicetype
from dcim.models import Site, Device, DeviceType

# ==============================================================================
# Global Variables
# ==============================================================================

# ==============================================================================
# Custom Templates
# ==============================================================================

IMAGE_SIZE = """
{% if record.image_exists %}
    {{ record.image.size|filesizeformat }}
{% else %}
    <span>&mdash;</span>
{% endif %}
"""

# ==============================================================================

IMAGE_MD5SUM = """
{% if record.md5sum == record.md5sum_calculated %}
    <span class="badge text-bg-green">{{ record.md5sum }}</span>
{% else %}
    <span class="badge text-bg-red">{{ record.md5sum }}</span>
{% endif %}
"""

# ==============================================================================

IMAGE_MD5SUM_CALCULATED = """
<span class="badge text-bg-green">{{ record.md5sum_calculated }}</span>
"""

# ==============================================================================
# Tables
# ==============================================================================


class ImageTable(NetBoxTable):

    filename = tables.Column(linkify=True)

    md5sum = TemplateColumn(
        verbose_name="md5sum expected", template_code=IMAGE_MD5SUM, orderable=False
    )

    md5sum_calculated = TemplateColumn(
        verbose_name="md5sum calculated",
        template_code=IMAGE_MD5SUM_CALCULATED,
        orderable=False,
    )

    status = ChoiceFieldColumn()

    size = TemplateColumn(
        verbose_name="size",
        template_code=IMAGE_SIZE,
        orderable=False,
    )

    class Meta(NetBoxTable.Meta):
        model = Image
        fields = (
            "pk",
            "id",
            "filename",
            "md5sum",
            "md5sum_calculated",
            "version",
            "description",
            "comments",
            "status",
            "size",
            "actions",
        )
        default_columns = ("pk", "filename", "version", "status", "size", "description")


# ==============================================================================


class GoldenImageTable(NetBoxTable):

    image = tables.Column(linkify=True)

    version = tables.Column(accessor="image.version")

    class Meta(NetBoxTable.Meta):
        model = GoldenImage
        fields = (
            "pk",
            "id",
            "name",
            "image",
            "version",
            "description",
            "comments",
            "regions",
            "site_groups",
            "sites",
            "locations",
            "device_types",
            "roles",
            "platforms",
            "tags",
            "actions",
        )
        default_columns = ("pk", "name", "image", "version", "description")


# ==============================================================================


class ImageDistributionServerTable(NetBoxTable):

    ip = tables.Column(linkify=True)

    download_method = ChoiceFieldColumn()

    class Meta(NetBoxTable.Meta):
        model = ImageDistributionServer
        fields = (
            "pk",
            "id",
            "ip",
            "name",
            "description",
            "comments",
            "download_method",
            "custom_port",
            "actions",
        )
        default_columns = (
            "pk",
            "ip",
            "name",
            "description",
            "download_method",
            "custom_port",
        )


# ==============================================================================


class SettingsDeviceTypeTable(NetBoxTable):

    device_type = tables.Column(linkify=True)

    device_remote_filesystem = ChoiceFieldColumn()

    device_upgrade_mode = ChoiceFieldColumn()

    class Meta(NetBoxTable.Meta):
        model = SettingsDeviceType
        fields = (
            "pk",
            "id",
            "device_type",
            "device_remote_filesystem",
            "device_upgrade_mode",
            "max_attempts_after_reload",
            "seconds_between_attemps_after_reload",
            "minutes_image_add_timeout",
            "minutes_image_activation_timeout",
            "actions",
        )
        default_columns = (
            "pk",
            "device_type",
            "device_remote_filesystem",
            "device_upgrade_mode",
            "max_attempts_after_reload",
            "seconds_between_attemps_after_reload",
            "minutes_image_add_timeout",
            "minutes_image_activation_timeout",
        )


# ==============================================================================
