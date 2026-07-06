import os
import time

import psutil


class SystemMonitor:
    """Collect Linux system health information."""

    def get_cpu_usage(self) -> float:
        """Return CPU usage percentage."""
        return psutil.cpu_percent(interval=1)

    def get_memory_usage(self) -> float:
        """Return memory usage percentage."""
        return psutil.virtual_memory().percent

    def get_disk_usage(self) -> float:
        """Return disk usage percentage for root filesystem."""
        return psutil.disk_usage("/").percent

    def get_load_average(self):
        """Return 1, 5 and 15 minute load average."""
        return os.getloadavg()

    def get_uptime(self) -> str:
        """Return system uptime in days, hours and minutes."""
        uptime_seconds = time.time() - psutil.boot_time()

        days = int(uptime_seconds // 86400)
        hours = int((uptime_seconds % 86400) // 3600)
        minutes = int((uptime_seconds % 3600) // 60)

        return f"{days} days, {hours} hours, {minutes} minutes"