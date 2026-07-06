import json
from datetime import datetime
from pathlib import Path


class ReportGenerator:
    """Generate JSON health reports."""

    def generate(self, report_data: dict) -> None:
        reports_dir = Path("reports")
        reports_dir.mkdir(exist_ok=True)

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

        report_file = reports_dir / f"health_report_{timestamp}.json"

        with open(report_file, "w", encoding="utf-8") as file:
            json.dump(report_data, file, indent=4)

        print(f"\nReport saved: {report_file}")