# ==============================================================================
# Imports
# ==============================================================================


from netbox.api.viewsets import NetBoxModelViewSet

# from .. import filtersets
from ..models import (
    Image,
)
from .serializers import (
    ImageSerializer,
)


# ==============================================================================
# View Sets
# ==============================================================================


class ImageViewSet(NetBoxModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    # filterset_class = filtersets.SWMGImageFilterSet
