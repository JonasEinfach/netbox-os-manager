from utilities.choices import ChoiceSet


"""
Choices for Upgrade Device
Choices not changeable by admin via configuration.py
"""


class SettingsDeviceFilesystemChoices(ChoiceSet):
    FILESYSTEM_BOOTFLASH = "bootflash:"
    FILESYSTEM_SDFLASH = "sdflash:"

    CHOICES = [
        (FILESYSTEM_BOOTFLASH, "bootflash:", "teal"),
        (FILESYSTEM_SDFLASH, "sdflash:", "pink"),
    ]


"""
# Choices for Upgrade Device
# Choices not changeable by admin via configuration.py
"""


class SettingsDeviceUpgradeModeChoices(ChoiceSet):
    UPGRADE_INSTALL_MODE = "INSTALL_MODE"
    # UPGRADE_BUNDLE_MODE = "BUNDLE_MODE"
    # Bundle mode is still not supported

    CHOICES = [
        (UPGRADE_INSTALL_MODE, "INSTALL_MODE", "green"),
        # (UPGRADE_BUNDLE_MODE, "BUNDLE_MODE", "orange"),
    ]
