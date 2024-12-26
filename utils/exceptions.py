class ScraperException(Exception):
    """Exception raised for errors specific to the scraper service."""
    def __init__(self, message: str = "An error occurred in the scraper service.", *args):
        super().__init__(message, *args)


class RegexException(Exception):
    """Exception raised for errors specific to regex processing."""
    def __init__(self, message: str = "An error occurred in regex processing.", *args):
        super().__init__(message, *args)


class ServiceUnavailableException(Exception):
    """Exception raised when an external service is unavailable."""
    def __init__(self, service_name: str = "The service", message: str = "is unavailable.", *args):
        self.service_name = service_name
        self.message = message
        super().__init__(f"{self.service_name} {self.message}", *args)
