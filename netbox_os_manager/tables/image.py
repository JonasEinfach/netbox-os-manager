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

from netbox_os_manager.models.image import *

__all__ = ["ImageTable"]

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

IMAGE_MD5SUM = """
{% if record.md5sum == record.md5sum_calculated %}
    <span class="badge text-bg-green">{{ record.md5sum }}</span>
{% else %}
    <span class="badge text-bg-red">{{ record.md5sum }}</span>
{% endif %}
"""

IMAGE_MD5SUM_CALCULATED = """
<span class="badge text-bg-green">{{ record.md5sum_calculated }}</span>
"""

# ==============================================================================
# Table
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
            "status",
            "size",
            "comments",
            "actions",
        )
        default_columns = ("pk", "filename", "version", "status", "size", "description")
