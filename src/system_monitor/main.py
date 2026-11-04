from system_monitor.memory import get_memory_report
from system_monitor.uptime import get_uptime_report
from system_monitor.disk import get_disk_report

def main():
    disk_path = "/"

    print ("Linux System Monitor")
    print()

    try:
        print ("Uptime")
        uptime_report = get_uptime_report()
    except FileNotFoundError:
        print (" Unable to read system uptime")
    else:
        print(f" {uptime_report}")

    print()
    try:
        print ("Memory")
        memory_report = get_memory_report()
    except FileNotFoundError:
        print (" Unable to read system memory")
    except ValueError:
        print (" Required memory data was invalid/missing")
    else:
        for line in memory_report:
            print (f" {line}")

    print()
    try:
        print (f"Disk ({disk_path})")
        disk_report = get_disk_report(disk_path)
    except FileNotFoundError:
        print (" Unable to read disk data")
    except ValueError:
        print (" Required disk data was invalid/missing")
    else:
        for line in disk_report:
            print (f" {line}")

if __name__== "__main__":
    main()