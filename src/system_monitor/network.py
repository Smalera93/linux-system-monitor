from system_monitor.formatting import LABEL_WIDTH, format_bytes

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

def format_network(total_received_bytes, total_transmitted_bytes):
     formatted_received_bytes = format_bytes(total_received_bytes)
     formatted_transmitted_bytes = format_bytes(total_transmitted_bytes)
     return (
          f"{'Received:':<{LABEL_WIDTH}} {formatted_received_bytes}",
          f"{'Sent:':<{LABEL_WIDTH}} {formatted_transmitted_bytes}", 
          )     

def get_network_report():
     total_received_bytes, total_transmitted_bytes = read_network_bytes()
     return format_network(total_received_bytes, total_transmitted_bytes)

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