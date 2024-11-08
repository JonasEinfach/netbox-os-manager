# ==============================================================================
# Imports
# ==============================================================================

from netbox.views import generic

# ==============================================================================
# Special Model Imports
# ==============================================================================

from .models import (
    Image,
    GoldenImage,
    ImageDistributionServer,
    SettingsDeviceType,
)

from .tables import (
    ImageTable,
    GoldenImageTable,
    ImageDistributionServerTable,
    SettingsDeviceTypeTable,
)

from .forms import (
    ImageForm,
    GoldenImageForm,
    ImageDistributionServerForm,
    SettingsDeviceTypeForm,
    SettingsDeviceTypeBulkEditForm,
)


# ==============================================================================
# Global Variables
# ==============================================================================

# ==============================================================================
# Views
# ==============================================================================


class ImageView(generic.ObjectView):
    queryset = Image.objects.all()


# ==============================================================================


class ImageListView(generic.ObjectListView):
    queryset = Image.objects.all()
    table = ImageTable

    actions = {
        "add": {"add"},
        "export": set(),
        "bulk_delete": {"delete"},
    }


# ==============================================================================


class ImageEditView(generic.ObjectEditView):
    queryset = Image.objects.all()
    form = ImageForm


# ==============================================================================


class ImageDeleteView(generic.ObjectDeleteView):
    queryset = Image.objects.all()


# ==============================================================================


class ImageBulkDeleteView(generic.BulkDeleteView):
    queryset = Image.objects.all()
    table = ImageTable


# ==============================================================================


class GoldenImageView(generic.ObjectView):
    queryset = GoldenImage.objects.all()

    def get_extra_context(self, request, instance):
        # Gather assigned objects for parsing in the template
        assigned_objects = (
            ("Regions", instance.regions.all),
            ("Site Groups", instance.site_groups.all),
            ("Sites", instance.sites.all),
            ("Locations", instance.locations.all),
            ("Device Types", instance.device_types.all),
            ("Roles", instance.roles.all),
            ("Platforms", instance.platforms.all),
        )

        return {
            "assigned_objects": assigned_objects,
        }


# ==============================================================================


class GoldenImageListView(generic.ObjectListView):
    queryset = GoldenImage.objects.all()
    table = GoldenImageTable


# ==============================================================================


class GoldenImageEditView(generic.ObjectEditView):
    queryset = GoldenImage.objects.all()
    form = GoldenImageForm


# ==============================================================================


class GoldenImageDeleteView(generic.ObjectDeleteView):
    queryset = GoldenImage.objects.all()


# ==============================================================================


class ImageDistributionServerView(generic.ObjectView):
    queryset = ImageDistributionServer.objects.all()


# ==============================================================================


class ImageDistributionServerListView(generic.ObjectListView):
    queryset = ImageDistributionServer.objects.all()
    table = ImageDistributionServerTable


# ==============================================================================


class ImageDistributionServerEditView(generic.ObjectEditView):
    queryset = ImageDistributionServer.objects.all()
    form = ImageDistributionServerForm


# ==============================================================================


class ImageDistributionServerDeleteView(generic.ObjectDeleteView):
    queryset = ImageDistributionServer.objects.all()


# ==============================================================================


class SettingsDeviceTypeView(generic.ObjectView):
    queryset = SettingsDeviceType.objects.all()


# ==============================================================================


class SettingsDeviceTypeListView(generic.ObjectListView):
    queryset = SettingsDeviceType.objects.all()
    table = SettingsDeviceTypeTable


# ==============================================================================


class SettingsDeviceTypeEditView(generic.ObjectEditView):
    queryset = SettingsDeviceType.objects.all()
    form = SettingsDeviceTypeForm


# ==============================================================================


class SettingsDeviceTypeBulkEditView(generic.BulkEditView):
    queryset = SettingsDeviceType.objects.all()
    table = SettingsDeviceTypeTable
    form = SettingsDeviceTypeBulkEditForm


# ==============================================================================


class SettingsDeviceTypeDeleteView(generic.ObjectDeleteView):
    queryset = SettingsDeviceType.objects.all()


# ==============================================================================


class SettingsDeviceTypeBulkDeleteView(generic.BulkDeleteView):
    queryset = SettingsDeviceType.objects.all()
    table = SettingsDeviceTypeTable


# ==============================================================================
