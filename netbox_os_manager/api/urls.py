# ==============================================================================
# Imports
# ==============================================================================

from netbox.api.routers import NetBoxRouter
from . import views

# ==============================================================================
# Special Model Imports
# ==============================================================================

# ==============================================================================
# GLOBAL VARS
# ==============================================================================


app_name = "netbox_os_manager"


# ==============================================================================
# NetboxRouter
# ==============================================================================


router = NetBoxRouter()
router.register("images", views.ImageViewSet)
router.register("goldenimages", views.GoldenImageViewSet)
router.register("imagedistributionservers", views.ImageDistributionServerViewSet)
router.register("settingsdevicetypes", views.SettingsDeviceTypeViewSet)

urlpatterns = router.urls
