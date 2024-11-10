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

from netbox_os_manager.models.settingsdevicetype import *

__all__ = ["SettingsDeviceTypeTable"]

# ==============================================================================
# Table
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
            "version_cli_show_command",
            "version_regex_search",
            "version_regex_group_index",
            "comments",
            "actions",
        )
        default_columns = (
            "pk",
            "device_type",
            "device_remote_filesystem",
            "device_upgrade_mode",
        )
