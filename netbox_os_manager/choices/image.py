from utilities.choices import ChoiceSet


class ImageStatusChoices(ChoiceSet):
    IMAGE_STATUS_UNKOWN = "unkown"
    IMAGE_STATUS_ACTIVE = "active"
    IMAGE_STATUS_ERROR_MD5_MISMATCH = "error md5 mismatch"

    CHOICES = [
        (IMAGE_STATUS_UNKOWN, "Unkown", "black"),
        (IMAGE_STATUS_ACTIVE, "Active", "green"),
        (IMAGE_STATUS_ERROR_MD5_MISMATCH, "Error-MD5-Mismatch", "red"),
    ]
