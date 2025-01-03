from utilities.choices import ChoiceSet

__all__ = ["ImageDistributionServerDownloadMethodChoices"]


class ImageDistributionServerDownloadMethodChoices(ChoiceSet):
    DOWNLOAD_METHOD_HTTP = "http"
    DOWNLOAD_METHOD_FTP = "ftp"

    CHOICES = [
        (DOWNLOAD_METHOD_HTTP, "HTTP", "teal"),
        (DOWNLOAD_METHOD_FTP, "FTP", "pink"),
    ]
