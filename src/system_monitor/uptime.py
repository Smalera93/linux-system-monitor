total_seconds = int(12315.79)
hours = total_seconds // 3600
remaining_seconds = total_seconds % 3600
minutes = remaining_seconds // 60
seconds = remaining_seconds % 60

print ('System uptime: %d hours, %d minutes, %d seconds' % (hours, minutes, seconds))
