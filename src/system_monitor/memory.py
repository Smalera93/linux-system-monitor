def read_memory():
    total_kib = None
    available_kib = None
    with open('/proc/meminfo', 'r') as memory_file:
        for line in memory_file:
            if line.startswith("MemTotal:"):
                raw_mem_total_line = line.split()
                raw_mem_total = raw_mem_total_line[1]
                total_kib = int(raw_mem_total)
            elif line.startswith("MemAvailable:"):
                raw_mem_available_line = line.split()
                raw_mem_available = raw_mem_available_line[1]
                available_kib = int(raw_mem_available)
        if total_kib is None or available_kib is None:
            raise ValueError ("Required field missing from /proc/meminfo")
        return total_kib, available_kib

def calculate_memory_usage(total_kib, available_kib):
    used_kib = total_kib - available_kib
    return used_kib

def kib_to_gib(value_kib):
    value_mib = value_kib / 1024
    value_gib = value_mib / 1024
    return value_gib

def calculate_memory_percent(total_kib, used_kib):
    if total_kib <= 0 or used_kib > total_kib or used_kib < 0:
        raise ValueError ("Invalid memory values")
    usage_percent = used_kib / total_kib * 100
    return usage_percent

def main():
    try:
        total_kib, available_kib = read_memory()
    except FileNotFoundError:
        print ('Unable to read system memory')
    except ValueError:
        print ('Required memory data was invalid/missing')
    else:
        used_kib = calculate_memory_usage(total_kib, available_kib)
        total_gib = kib_to_gib(total_kib)
        available_gib = kib_to_gib(available_kib)
        used_gib = kib_to_gib(used_kib)
        print('Total: %.2f GiB' % (total_gib))
        print('Available: %.2f GiB' % (available_gib))
        print('Used: %.2f GiB' % (used_gib))
        percent = calculate_memory_percent(total_kib, used_kib)
        print('Percent usage: %.1f%%' % (percent))

if __name__== "__main__":
    main()