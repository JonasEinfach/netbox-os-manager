# ==============================================================================
# Imports
# ==============================================================================

from netbox.views import generic

from netbox_os_manager.models.settingsdevicetype import *
from netbox_os_manager.tables.settingsdevicetype import *
from netbox_os_manager.forms.settingsdevicetype import *

# Custom stuff
from dcim.tables import DeviceTable
from dcim.models import Device

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

    def get_extra_context(self, request, instance):
        # Gather all device from the device type to display all devices
        table = DeviceTable(Device.objects.filter(device_type=instance.device_type))
        table.configure(request)

        device_count = len(Device.objects.filter(device_type=instance.device_type))

        return {"device_table": table, "device_count": device_count}


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
