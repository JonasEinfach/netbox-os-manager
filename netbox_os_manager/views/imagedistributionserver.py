# ==============================================================================
# Imports
# ==============================================================================

from netbox.views import generic

from netbox_os_manager.models.imagedistributionserver import *
from netbox_os_manager.tables.imagedistributionserver import *
from netbox_os_manager.forms.imagedistributionserver import *

__all__ = [
    "ImageDistributionServerView",
    "ImageDistributionServerListView",
    "ImageDistributionServerEditView",
    "ImageDistributionServerDeleteView",
]

# ==============================================================================
# Views
# ==============================================================================


class ImageDistributionServerView(generic.ObjectView):
    queryset = ImageDistributionServer.objects.all()


class ImageDistributionServerListView(generic.ObjectListView):
    queryset = ImageDistributionServer.objects.all()
    table = ImageDistributionServerTable


class ImageDistributionServerEditView(generic.ObjectEditView):
    queryset = ImageDistributionServer.objects.all()
    form = ImageDistributionServerForm


class ImageDistributionServerDeleteView(generic.ObjectDeleteView):
    queryset = ImageDistributionServer.objects.all()
