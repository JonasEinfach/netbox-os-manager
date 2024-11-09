# ==============================================================================
# Imports
# ==============================================================================

from netbox.filtersets import NetBoxModelFilterSet
from django.db.models import Q
import django_filters

from netbox_os_manager.models.image import *

__all__ = ["ImageFilterSet"]

# ==============================================================================
# Filtersets
# ==============================================================================


class ImageFilterSet(NetBoxModelFilterSet):

    filename = django_filters.CharFilter(
        method="search",
    )

    version = django_filters.CharFilter(
        method="search",
    )

    description = django_filters.CharFilter(
        method="search",
    )

    def search(self, queryset, name, value):
        if not value.strip():
            return queryset
        return queryset.filter(
            Q(filename__icontains=value)
            | Q(description__icontains=value)
            | Q(version__icontains=value)
        )

    class Meta:
        model = Image
        fields = ("id", "filename", "version", "status", "description")
