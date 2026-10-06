def read_uptime_seconds():
    with open('/proc/uptime', 'r') as uptime_file:
        raw_uptime = uptime_file.read()
    uptime_fields = raw_uptime.split()
    uptime_seconds = float(uptime_fields[0])
    total_seconds = int(uptime_seconds)
    return total_seconds

def seconds_to_hms(total_seconds):
    hours = total_seconds // 3600
    remaining_seconds = total_seconds % 3600
    minutes = remaining_seconds // 60
    seconds = remaining_seconds % 60
    return (hours, minutes, seconds)

try:
    total_seconds = read_uptime_seconds()
except FileNotFoundError:
    print ('Unable to read system uptime')
else:
    hours, minutes, seconds = seconds_to_hms(total_seconds)
    print('System uptime: %d hours, %d minutes, %d seconds' % (hours, minutes, seconds))
