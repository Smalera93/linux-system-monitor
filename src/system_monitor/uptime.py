with open('/proc/uptime', 'r') as uptime_file:
        raw_uptime = uptime_file.read()
uptime_fields = raw_uptime.split()
uptime_seconds = float(uptime_fields[0])

total_seconds = int(uptime_seconds)
hours = total_seconds // 3600
remaining_seconds = total_seconds % 3600
minutes = remaining_seconds // 60
seconds = remaining_seconds % 60

print('System uptime: %d hours, %d minutes, %d seconds' % (hours, minutes, seconds))
