# ==============================================================================
# Imports
# ==============================================================================

from netbox.search import SearchIndex, register_search

from netbox_os_manager.models import *

# ==============================================================================
# Searchs
# ==============================================================================


@register_search
class ImageIndex(SearchIndex):
    model = Image
    fields = (
        ("filename", 100),
        ("version", 150),
        ("description", 2000),
        ("comments", 5000),
    )

    display_attrs = ("filename", "status", "version", "description", "comments")


@register_search
class GoldenImageIndex(SearchIndex):
    model = GoldenImage
    fields = (
        ("name", 100),
        ("description", 2000),
        ("device_types", 3000),
        ("comments", 5000),
    )

    display_attrs = ("name", "image", "description", "comments")


@register_search
class ImageDistributionServerIndex(SearchIndex):
    model = ImageDistributionServer
    fields = (
        ("name", 100),
        ("ip", 200),
        ("description", 2000),
        ("comments", 5000),
    )

    display_attrs = (
        "name",
        "ip",
        "description",
        "comments",
        "download_method",
        "custom_port",
    )


@register_search
class SettingsDeviceTypeIndex(SearchIndex):
    model = SettingsDeviceType
    fields = (
        ("device_type", 100),
        ("comments", 5000),
    )

    display_attrs = (
        "device_type",
        "device_remote_filesystem",
        "device_upgrade_mode",
        "comments",
    )
