class HealthEvaluator:
    """
    Evaluate system health using configured thresholds.
    """

    def evaluate(self, value: float, threshold: int) -> str:
        """
        Compare a metric against its threshold.
        """

        if value > threshold:
            return "CRITICAL"

        elif value == threshold:
            return "WARNING"

        return "HEALTHY"