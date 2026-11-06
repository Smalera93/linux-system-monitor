from system_monitor.formatting import LABEL_WIDTH
import time

def read_cpu_times():
    with open('/proc/stat', 'r') as cpu_times_file:
        for line in cpu_times_file:
            if line.startswith("cpu "):
                cpu_times_line = line.split()
                cpu_times_user = int(cpu_times_line[1])
                cpu_times_nice = int(cpu_times_line[2])
                cpu_times_system = int(cpu_times_line[3])
                cpu_times_idle = int(cpu_times_line[4])
                cpu_times_iowait = int(cpu_times_line[5])
                cpu_times_irq = int(cpu_times_line[6])
                cpu_times_softirq = int(cpu_times_line[7])
                cpu_times_steal = int(cpu_times_line[8])             
        return (
            cpu_times_user, 
            cpu_times_nice, 
            cpu_times_system, 
            cpu_times_idle, 
            cpu_times_iowait, 
            cpu_times_irq, 
            cpu_times_softirq, 
            cpu_times_steal,
        )

def calculate_cpu_usage(first_sample, second_sample):
    first_user, first_nice, first_system, first_idle, first_iowait, first_irq, first_softirq, first_steal = first_sample
    second_user, second_nice, second_system, second_idle, second_iowait, second_irq, second_softirq, second_steal = second_sample
    
    first_total_time = first_user + first_nice + first_system + first_idle + first_iowait + first_irq + first_softirq + first_steal
    second_total_time = second_user + second_nice + second_system + second_idle + second_iowait + second_irq + second_softirq + second_steal
    
    first_idle_time = first_idle + first_iowait
    second_idle_time = second_idle + second_iowait
    
    total_delta = second_total_time - first_total_time

    if total_delta <= 0:
        raise ValueError("Invalid CPU sample interval")
    
    idle_delta = second_idle_time - first_idle_time
    busy_delta = total_delta - idle_delta
    
    usage_percent = busy_delta / total_delta * 100
    return usage_percent

def get_cpu_usage():
    first_sample = read_cpu_times()
    time.sleep(1)
    second_sample = read_cpu_times()
    usage_percent = calculate_cpu_usage(first_sample, second_sample)
    return usage_percent

def format_cpu(usage_percent):
    return (f"{'Usage:':<{LABEL_WIDTH}} {usage_percent:.1f}%")

def get_cpu_report():
    cpu_report = format_cpu(get_cpu_usage())
    return cpu_report

def main():
    try:
        print ("CPU")
        cpu_report = get_cpu_report()
    except FileNotFoundError:
        print (" Unable to read CPU values")
    except ValueError:
        print ("Invalid CPU sample interval")
    else:
        print(f" {cpu_report}")

if __name__== "__main__":
    main()