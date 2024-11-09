# ==============================================================================
# Imports
# ==============================================================================

from netbox.views import generic

from netbox_os_manager.models.settingsdevicetype import *
from netbox_os_manager.tables.settingsdevicetype import *
from netbox_os_manager.forms.settingsdevicetype import *

__all__ = [
    "SettingsDeviceTypeView",
    "SettingsDeviceTypeListView",
    "SettingsDeviceTypeEditView",
    "SettingsDeviceTypeBulkEditView",
    "SettingsDeviceTypeDeleteView",
    "SettingsDeviceTypeBulkDeleteView",
]

# ==============================================================================
# Views
# ==============================================================================


class SettingsDeviceTypeView(generic.ObjectView):
    queryset = SettingsDeviceType.objects.all()


class SettingsDeviceTypeListView(generic.ObjectListView):
    queryset = SettingsDeviceType.objects.all()
    table = SettingsDeviceTypeTable


class SettingsDeviceTypeEditView(generic.ObjectEditView):
    queryset = SettingsDeviceType.objects.all()
    form = SettingsDeviceTypeForm


class SettingsDeviceTypeBulkEditView(generic.BulkEditView):
    queryset = SettingsDeviceType.objects.all()
    table = SettingsDeviceTypeTable
    form = SettingsDeviceTypeBulkEditForm


class SettingsDeviceTypeDeleteView(generic.ObjectDeleteView):
    queryset = SettingsDeviceType.objects.all()


class SettingsDeviceTypeBulkDeleteView(generic.BulkDeleteView):
    queryset = SettingsDeviceType.objects.all()
    table = SettingsDeviceTypeTable
