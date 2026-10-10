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

def format_time_unit(value, singular_label):
    if value == 1:
        return '%d %s' % (value, singular_label)
    else:
        return '%d %ss' % (value, singular_label)

try:
    total_seconds = read_uptime_seconds()
except FileNotFoundError:
    print ('Unable to read system uptime')
else:
    hours, minutes, seconds = seconds_to_hms(total_seconds)
    uptime_parts = []
    if hours != 0:
        uptime_parts.append(format_time_unit(hours, 'hour'))
    if minutes != 0:
        uptime_parts.append(format_time_unit(minutes, 'minute'))
    if seconds != 0:
        uptime_parts.append(format_time_unit(seconds, 'second'))
    if len(uptime_parts) == 1:
        print ('System uptime: %s' % (uptime_parts[0]))
    elif len(uptime_parts) == 0:
        print ('System uptime: 0 seconds')
    else:
        initial_units = uptime_parts[:-1]
        formatted_initial_units = ', '.join(initial_units)
        last_unit = uptime_parts[-1]
        print('System uptime: %s and %s' % (formatted_initial_units, last_unit))
