import time
from threading import Thread

def square(n):
    print("square of {} is:{}\n".format(n,n*n))

start_time = time.time()
threads =[]
for num in range(1,101):
    t=Thread(target=square,args=(num,))
    threads.append(t)
    t.start()
#wait for the threads to compleat
for t in threads:
    t.join()

end_time = time.time()

print(f"it took{end_time-start_time:0.2f}seconds to compleat:")