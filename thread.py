import time
from threading import Thread

def task():
    print("starting a task....\n")
    time.sleep(1)
    print("done\n")

start_time = time.time()
#create two new threads
t1=Thread(target=task)
t2=Thread(target=task)
#start the threads
t1.start()
t2.start()
#wait for the thread to complete
t1.join()
t2.join()
end_time = time.time()

print(f"it took{end_time-start_time:0.2f}second to compleat")