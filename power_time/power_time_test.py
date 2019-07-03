import time
start_time = time.ctime(time.time())
while True:
    with open('power_log', 'w') as f:
        print(start_time, time.ctime(time.time()), file=f)
    time.sleep(60 * 5)
