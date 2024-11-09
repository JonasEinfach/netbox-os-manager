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

from netbox_os_manager.models.imagedistributionserver import *

__all__ = ["ImageDistributionServerTable"]

# ==============================================================================
# Table
# ==============================================================================


class ImageDistributionServerTable(NetBoxTable):

    ip = tables.Column(linkify=True)
    name = tables.Column(linkify=True)
    download_method = ChoiceFieldColumn()

    class Meta(NetBoxTable.Meta):
        model = ImageDistributionServer
        fields = (
            "pk",
            "id",
            "ip",
            "name",
            "description",
            "download_method",
            "custom_port",
            "comments",
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
