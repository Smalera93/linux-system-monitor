from system_monitor.formatting import LABEL_WIDTH, format_bytes
import time

def read_network_bytes():
    with open('/proc/net/dev', 'r') as network_bytes_file:
       
        total_received_bytes = 0
        total_transmitted_bytes = 0
        
        for line in network_bytes_file:
                if ":" not in line:
                     continue
               
                interface, data = line.split(":", 1)
                interface = interface.strip()
                
                if interface == "lo":
                     continue
               
                values = data.split()
                total_received_bytes += int(values[0])
                total_transmitted_bytes += int(values[8])
    
    return total_received_bytes, total_transmitted_bytes

def calculate_network_rate(first_sample, second_sample, interval_seconds):
    if interval_seconds <= 0:
        raise ValueError("Interval seconds must be more than 0")
    
    first_received, first_transmitted = first_sample
    second_received, second_transmitted = second_sample
    
    if second_received < first_received or second_transmitted < first_transmitted:
        raise ValueError("Network counters decreased between samples")
    
    received_delta = second_received - first_received
    transmitted_delta = second_transmitted - first_transmitted
   
    received_rate = received_delta / interval_seconds
    transmitted_rate = transmitted_delta / interval_seconds
    
    return received_rate, transmitted_rate

def get_network_stats(interval_seconds):
    first_sample = read_network_bytes()
    time.sleep(interval_seconds)
    second_sample = read_network_bytes()
    received_rate, transmitted_rate = calculate_network_rate(first_sample, second_sample, interval_seconds)
    latest_received_total, latest_transmitted_total = second_sample
    return latest_received_total, latest_transmitted_total, received_rate, transmitted_rate

def format_network(
        total_received_bytes, 
        total_transmitted_bytes,
        received_rate,
        transmitted_rate,
        ):
   
    formatted_received_bytes = format_bytes(total_received_bytes)
    formatted_transmitted_bytes = format_bytes(total_transmitted_bytes)
    formatted_received_rate = format_bytes(received_rate)
    formatted_transmitted_rate = format_bytes(transmitted_rate)
    
    return (
          f"{'Received:':<{LABEL_WIDTH}} {formatted_received_bytes}",
          f"{'Sent:':<{LABEL_WIDTH}} {formatted_transmitted_bytes}",
          f"{'Download:':<{LABEL_WIDTH}} {formatted_received_rate}/s",
          f"{'Upload:':<{LABEL_WIDTH}} {formatted_transmitted_rate}/s",
          )     

def get_network_report(interval_seconds=1):
    (
        total_received_bytes,
        total_transmitted_bytes,
        received_rate,
        transmitted_rate,
    ) = get_network_stats(interval_seconds)
    return format_network(
        total_received_bytes, 
        total_transmitted_bytes,
        received_rate,
        transmitted_rate,     
        )

def main():
    try:
        print("Network")
        network_report = get_network_report()
    except FileNotFoundError:
        print(" Unable to read network values")
    except ValueError:
        print(" Invalid network values")
    else:
        for line in network_report:
            print(f" {line}")

if __name__== "__main__":
    main()