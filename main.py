
import time

def clock():
    while True:
        current_time = time.strftime("%H:%M:%S") 
        print(current_time, end="\r")
        time.sleep(1)

clock()

    # Press Ctrl+C to stop the program.