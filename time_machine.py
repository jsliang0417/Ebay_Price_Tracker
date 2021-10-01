###Scheduling running script
from datetime import datetime
import time
import sys
from apscheduler.schedulers.background import BackgroundScheduler

#input_time = int(sys.argv[1])


def say_Hi_Every_5_seconds(text):
    print(text)
    print('Hello')
    

# if __name__ == '__main__':
    
    
def trigger(func, description, input_time):
    scheduler = BackgroundScheduler()
    scheduler.add_job(func, 'cron', [description], second="*/{0}".format(input_time))
    scheduler.start()
    print('Press ctrl + c to terminate the script.')

    try:
        # This is here to simulate application activity (which keeps the main thread alive).
        while True:
            time.sleep(1)
    except (KeyboardInterrupt, SystemExit):
        # Not strictly necessary if daemonic mode is enabled but should be done if possible
        scheduler.shutdown()


# trigger(say_Hi_Every_5_seconds, input_time)
        

"""
Thinking:
    1. receive the time input by the user
    2. string processing, extract and convert to parameter supported time format
    3. pass in the time to trigger the scheduler
"""
