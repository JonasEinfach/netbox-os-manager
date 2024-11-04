# ==============================================================================
# Imports
# ==============================================================================


from netbox.api.viewsets import NetBoxModelViewSet

# from .. import filtersets
from ..models import Image, GoldenImage, ImageDistributionServer, SettingsDeviceType
from .serializers import (
    ImageSerializer,
    GoldenImageSerializer,
    ImageDistributionServerSerializer,
    SettingsDeviceTypeSerializer,
)


# ==============================================================================
# View Sets
# ==============================================================================


class ImageViewSet(NetBoxModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    # filterset_class = filtersets.SWMGImageFilterSet


class GoldenImageViewSet(NetBoxModelViewSet):
    queryset = GoldenImage.objects.all()
    serializer_class = GoldenImageSerializer
    # filterset_class = filtersets.SWMGImageFilterSet


class ImageDistributionServerViewSet(NetBoxModelViewSet):
    queryset = ImageDistributionServer.objects.all()
    serializer_class = ImageDistributionServerSerializer
    # filterset_class = filtersets.SWMGImageFilterSet


class SettingsDeviceTypeViewSet(NetBoxModelViewSet):
    queryset = SettingsDeviceType.objects.all()
    serializer_class = SettingsDeviceTypeSerializer
    # filterset_class = filtersets.SWMGImageFilterSet
