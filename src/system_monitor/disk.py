import shutil
from system_monitor.formatting import LABEL_WIDTH

def read_disk_usage(path):
    disk_usage = shutil.disk_usage(path)
    total_bytes = disk_usage.total
    used_bytes = disk_usage.used
    free_bytes = disk_usage.free
    return total_bytes, used_bytes, free_bytes

def bytes_to_gib(value_bytes):
    value_kib = value_bytes / 1024
    value_mib = value_kib / 1024
    value_gib = value_mib / 1024
    return value_gib

def calculate_used_disk_percent(used_bytes, free_bytes):
    if used_bytes < 0 or free_bytes < 0 or used_bytes + free_bytes == 0:
        raise ValueError ("Invalid disk usage values")
    float_used_percentage = used_bytes / (used_bytes + free_bytes) * 100
    return float_used_percentage
        
def format_disk(total_gib, used_gib, free_gib, used_percent):
    return [
        f"{'Total:':<{LABEL_WIDTH}} {total_gib:.2f} GiB",
        f"{'Used:':<{LABEL_WIDTH}} {used_gib:.2f} GiB",
        f"{'Free:':<{LABEL_WIDTH}} {free_gib:.2f} GiB",
        f"{'Usage:':<{LABEL_WIDTH}} {used_percent:.1f}%"        
            ]

def get_disk_report(path):
    total_bytes, used_bytes, free_bytes = read_disk_usage(path)
    total_gib = bytes_to_gib(total_bytes)
    used_gib = bytes_to_gib(used_bytes)
    free_gib = bytes_to_gib(free_bytes)
    used_percentage = calculate_used_disk_percent(used_bytes, free_bytes)
    disk_report = format_disk(total_gib, used_gib, free_gib, used_percentage)
    return disk_report

def main():
    try:
        disk_report = get_disk_report("/")
    except FileNotFoundError:
        print ('Unable to read disk data')
    except ValueError:
        print ('Required disk data was invalid/missing')
    else:
        for line in disk_report:
            print (line)

if __name__== "__main__":
    main()