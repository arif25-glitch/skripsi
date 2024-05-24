import threading
import queue
import time

def worker(name, delay):
    print(f'{name} is start working')
    time.sleep(delay)
    print(f'{name} stopped working')

def worker_calculating(name, a, b, result_queue):
    print("=======================")
    print(f'{name} worker is starting tahi')
    result_queue.put(a * b)

result_queue1 = queue.Queue()
result_queue2 = queue.Queue()

thread1 = threading.Thread(target=worker, args=('worker_1', 4))
thread2 = threading.Thread(target=worker, args=('worker_2', 1))

worker_calc1 = threading.Thread(target=worker_calculating, args=('worker_calc_1', 2, 1, result_queue1))
worker_calc2 = threading.Thread(target=worker_calculating, args=('worker_calc_2', 6, 2, result_queue2))

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print("First workers are done!")
worker_calc1.start()
worker_calc2.start()

worker_calc1.join()
worker_calc2.join()

print(result_queue1.get() * result_queue2.get())


# setan algorithm
# import threading
# import time


# def mythread():
#     time.sleep(1000)

# def main():
#     threads = 0     #thread counter
#     y = 30000     #a MILLION of 'em!
#     for i in range(y):
#         try:
#             x = threading.Thread(target=mythread, daemon=True)
#             threads += 1    #thread counter
#             x.start()       #start each thread
#         except RuntimeError:    #too many throws a RuntimeError
#             break
#     print("{} threads created.\n".format(threads))

# if __name__ == "__main__":
#     main()