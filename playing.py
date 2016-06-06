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

def main():

    keep_looping = True
    while (keep_looping):
        # Get current status
        status = run_cmd("mpc status" )
        # Parse status to get time.
        print(status)
        # if playing update config.

        # Check every 5 seconds.
        sleep(5)
