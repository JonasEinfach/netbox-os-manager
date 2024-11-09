# ==============================================================================
# Imports
# ==============================================================================

from netbox.views import generic

from netbox_os_manager.models.image import *
from netbox_os_manager.tables.image import *
from netbox_os_manager.forms.image import *
from netbox_os_manager.filtersets.image import *

__all__ = [
    "ImageView",
    "ImageListView",
    "ImageEditView",
    "ImageDeleteView",
    "ImageBulkDeleteView",
]

# ==============================================================================
# Views
# ==============================================================================


class ImageView(generic.ObjectView):
    queryset = Image.objects.all()


class ImageListView(generic.ObjectListView):
    queryset = Image.objects.all()
    table = ImageTable
    filterset = ImageFilterSet
    filterset_form = ImageFilterForm

    actions = {
        "add": {"add"},
        "export": set(),
        "bulk_delete": {"delete"},
    }


class ImageEditView(generic.ObjectEditView):
    queryset = Image.objects.all()
    form = ImageForm


class ImageDeleteView(generic.ObjectDeleteView):
    queryset = Image.objects.all()


class ImageBulkDeleteView(generic.BulkDeleteView):
    queryset = Image.objects.all()
    table = ImageTable
