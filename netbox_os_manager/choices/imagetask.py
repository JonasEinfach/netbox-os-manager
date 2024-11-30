from utilities.choices import ChoiceSet

__all__ = ["ImageTaskLogSubStatusChoices", "ImageTaskLogLevelChoices"]

"""
Choices for Image Task Log Sub Status
Choices not changeable by admin via configuration.py
"""


class ImageTaskLogSubStatusChoices(ChoiceSet):
    STATUS_UNKNOWN = "unknown"
    STATUS_RUNNING = "running"
    STATUS_SUCCEEDED = "succeeded"
    STATUS_WARNING = "warning"
    STATUS_ERROR = "error"
    CHOICES = [
        (STATUS_UNKNOWN, "Unknown", "white"),
        (STATUS_RUNNING, "Running", "pink"),
        (STATUS_SUCCEEDED, "Succeeded", "green"),
        (STATUS_WARNING, "Warning", "orange"),
        (STATUS_ERROR, "Error", "red"),
    ]


"""
Choices for Image Task Log Level
Choices not changeable by admin via configuration.py
"""


class ImageTaskLogLevelChoices(ChoiceSet):
    LOG_LEVEL_UNKOWN = "unkown"
    LOG_LEVEL_INFO = "info"
    LOG_LEVEL_WARNING = "warning"
    LOG_LEVEL_ERROR = "error"
    LOG_LEVEL_DEBUG = "debug"
    CHOICES = [
        (LOG_LEVEL_UNKOWN, "Unknown", "white"),
        (LOG_LEVEL_INFO, "Info", "yellow"),
        (LOG_LEVEL_WARNING, "Warning", "orange"),
        (LOG_LEVEL_ERROR, "Error", "red"),
        (LOG_LEVEL_DEBUG, "Debug", "pink"),
    ]
