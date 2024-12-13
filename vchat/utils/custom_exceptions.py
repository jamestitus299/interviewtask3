class RateLimitExceeded(Exception):
    """Custom exception for rate limit exceeded"""
    def __init__(self, message: str = "Rate limit exceeded."):
        self.message = message
        super().__init__(self.message)