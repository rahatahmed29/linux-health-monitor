from config import Config
from health import HealthEvaluator
from logger import setup_logger
from monitor import SystemMonitor
from service_monitor import ServiceMonitor


def main():

    logger = setup_logger()

    config = Config()

    monitor = SystemMonitor()

    service_monitor = ServiceMonitor()

    evaluator = HealthEvaluator()

    logger.info("Linux Health Monitor Started")

    cpu = monitor.get_cpu_usage()
    memory = monitor.get_memory_usage()
    disk = monitor.get_disk_usage()
    load = monitor.get_load_average()
    uptime = monitor.get_uptime()

    cpu_status = evaluator.evaluate(
        cpu,
        config.get("cpu_threshold"),
    )

    memory_status = evaluator.evaluate(
        memory,
        config.get("memory_threshold"),
    )

    disk_status = evaluator.evaluate(
        disk,
        config.get("disk_threshold"),
    )

    print("=" * 60)
    print("Linux Health Monitor")
    print("=" * 60)

    print(f"CPU Usage      : {cpu}%   [{cpu_status}]")
    print(f"Memory Usage   : {memory}%   [{memory_status}]")
    print(f"Disk Usage     : {disk}%   [{disk_status}]")
    print(f"Load Average   : {load}")
    print(f"Uptime         : {uptime}")

    logger.info(f"CPU Usage: {cpu}% [{cpu_status}]")
    logger.info(f"Memory Usage: {memory}% [{memory_status}]")
    logger.info(f"Disk Usage: {disk}% [{disk_status}]")

    print("\nServices")
    print("-" * 30)

    services = config.get("services")

    for service in services:
        status = service_monitor.check_service(service)
        print(f"{service:<12}: {status}")
        logger.info(f"{service}: {status}")

    overall = "HEALTHY"

    if (
        cpu_status == "CRITICAL"
        or memory_status == "CRITICAL"
        or disk_status == "CRITICAL"
    ):
        overall = "CRITICAL"

    print("\nOverall Health")
    print("-" * 30)
    print(overall)

    logger.info(f"Overall Health: {overall}")

    logger.info("Linux Health Monitor Finished")


if __name__ == "__main__":
    main()