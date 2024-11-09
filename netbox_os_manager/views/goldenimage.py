# ==============================================================================
# Imports
# ==============================================================================

from netbox.views import generic

from netbox_os_manager.models.goldenimage import *
from netbox_os_manager.tables.goldenimage import *
from netbox_os_manager.forms.goldenimage import *

__all__ = [
    "GoldenImageView",
    "GoldenImageListView",
    "GoldenImageEditView",
    "GoldenImageDeleteView",
]

# ==============================================================================
# Views
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


class GoldenImageListView(generic.ObjectListView):
    queryset = GoldenImage.objects.all()
    table = GoldenImageTable


class GoldenImageEditView(generic.ObjectEditView):
    queryset = GoldenImage.objects.all()
    form = GoldenImageForm


class GoldenImageDeleteView(generic.ObjectDeleteView):
    queryset = GoldenImage.objects.all()
