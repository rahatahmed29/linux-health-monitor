from monitor import SystemMonitor
from service_monitor import ServiceMonitor
from config import Config

def main():
    monitor = SystemMonitor()

    print("=" * 40)
    print(" Linux Health Monitor")
    print("=" * 40)

    print(f"CPU Usage      : {monitor.get_cpu_usage()} %")
    print(f"Memory Usage   : {monitor.get_memory_usage()} %")
    print(f"Disk Usage     : {monitor.get_disk_usage()} %")
    print(f"Load Average   : {monitor.get_load_average()}")
    print(f"Uptime         : {monitor.get_uptime()}")

    print("=" * 40)


    config = Config()
    print("Configuration")
    print("-" * 20)
    print(f"CPU Threshold     : {config.get('cpu_threshold')}%")
    print(f"Disk Threshold    : {config.get('disk_threshold')}%")
    print(f"Memory Threshold  : {config.get('memory_threshold')}%")


    service_monitor = ServiceMonitor()
    print()
    print("Services")
    print("-" * 20)

    services = config.get("services")
    for service in services:
     status = service_monitor.check_service(service)
     print(f"{service:<10}: {status}")


if __name__ == "__main__":
    main()