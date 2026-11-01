from system_monitor.memory import get_memory_report
from system_monitor.uptime import get_uptime_report

def main():
    try:
        uptime_report = get_uptime_report()
    except FileNotFoundError:
        print ('Unable to read system uptime')
    else:
        print('System uptime: %s' % (uptime_report))

    try:
        memory_report = get_memory_report()
    except FileNotFoundError:
        print ('Unable to read system memory')
    except ValueError:
        print ('Required memory data was invalid/missing')
    else:
        for line in memory_report:
            print (line)

if __name__== "__main__":
    main()