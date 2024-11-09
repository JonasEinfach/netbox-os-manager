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

from netbox_os_manager.models.goldenimage import *

__all__ = ["GoldenImageTable"]

# ==============================================================================
# Table
# ==============================================================================


class GoldenImageTable(NetBoxTable):

    name = tables.Column(linkify=True)
    image = tables.Column(linkify=True)
    version = tables.Column(accessor="image.version")

    class Meta(NetBoxTable.Meta):
        model = GoldenImage
        fields = (
            "pk",
            "id",
            "name",
            "image",
            "weight",
            "version",
            "description",
            "regions",
            "site_groups",
            "sites",
            "locations",
            "device_types",
            "roles",
            "platforms",
            "comments",
            "actions",
        )
        default_columns = ("pk", "name", "image", "version", "description")
