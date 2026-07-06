from config import Config
from logger import setup_logger
from monitor import SystemMonitor
from service_monitor import ServiceMonitor


def main():

    logger = setup_logger()

    config = Config()

    monitor = SystemMonitor()

    service_monitor = ServiceMonitor()

    logger.info("Linux Health Monitor Started")

    cpu = monitor.get_cpu_usage()
    memory = monitor.get_memory_usage()
    disk = monitor.get_disk_usage()
    load = monitor.get_load_average()
    uptime = monitor.get_uptime()

    print("=" * 50)
    print("Linux Health Monitor")
    print("=" * 50)

    print(f"CPU Usage      : {cpu}%")
    print(f"Memory Usage   : {memory}%")
    print(f"Disk Usage     : {disk}%")
    print(f"Load Average   : {load}")
    print(f"Uptime         : {uptime}")

    logger.info(f"CPU Usage: {cpu}%")
    logger.info(f"Memory Usage: {memory}%")
    logger.info(f"Disk Usage: {disk}%")
    logger.info(f"Load Average: {load}")
    logger.info(f"Uptime: {uptime}")

    print("\nServices")
    print("-" * 25)

    services = config.get("services")

    for service in services:
        status = service_monitor.check_service(service)
        print(f"{service:<10}: {status}")
        logger.info(f"{service}: {status}")

    logger.info("Linux Health Monitor Finished")


if __name__ == "__main__":
    main()