import subprocess


class ServiceMonitor:
    """Check Linux service status."""

    def check_service(self, service_name: str) -> str:
        """
        Return service status.

        running
        stopped
        unavailable
        """

        try:
            result = subprocess.run(
                ["systemctl", "is-active", service_name],
                capture_output=True,
                text=True,
                check=False,
            )

            status = result.stdout.strip()

            if status == "active":
                return "Running"

            return "Stopped"

        except FileNotFoundError:
            return "systemctl not found"

        except Exception:
            return "Unavailable"