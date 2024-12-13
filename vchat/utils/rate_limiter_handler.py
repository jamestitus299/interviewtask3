from aiolimiter import AsyncLimiter
import asyncio


class RateLimitManager:
    """Manages rate limiting for the application"""
    def __init__(self, max_rate: int = 1, time_period: int = 60):
        """
        Initialize rate limiter
        
        Args:
            max_rate (int): Maximum number of requests allowed
            time_period (int): Time window in seconds
        """
        self._limiter = AsyncLimiter(max_rate, time_period)
        
    async def acquire(self) -> bool:
        """
        Attempt to acquire a rate limit token
        
        Returns:
            bool: True if token acquired, False if rate limited
        """
        print("---rate---")
        try:
            await self._limiter.acquire()
            return True
        except asyncio.TimeoutError:
            return False