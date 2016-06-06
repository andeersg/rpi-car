# Python script
#
# Check if mpc is available, if not exit
#
# Every 30 sec?
#   Check status of mpc
#   if playing, get file and time.
#   Update a database or json file or something
#
#
#
# Instead of the iPhone app use a web interface with sockets or something,
# that reads from the same db/file and controls mpc
import json;
from time import sleep

def main():

    debug_show = 'show1'
    debug_time = 1

    keep_looping = True
    while (keep_looping):
        # Get current status
        # status = run_cmd("mpc status" )
        # status = "testing"
        # Parse status to get time.
        print(debug_show + " - " + str(debug_time))
        # if playing update config.
        registerPlaytime(debug_show, debug_time)
        debug_time += 1
        # Check every 5 seconds.
        sleep(5)

def registerPlaytime(show, elapsed):
    json_data = open('config.json', 'r')
    data = json.load(json_data)

    data[show] = elapsed

    json_data = open('config.json', 'w+')
    json_data.write(json.dumps(data))
    json_data.close()



main()
