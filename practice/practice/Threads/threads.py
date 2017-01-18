import time
import thread


def print_func(thread_name, delay):
    count = 0
    while count < 5:
        time.sleep(delay)
        count += 1
        print "Executing thread {}, {} count.".format(thread_name, count)
try:
    thread.start_new_thread(print_func, ("thread_11", 3))
    thread.start_new_thread(print_func, ("thread_22", 3))
except:
    print "Caught exception"

while 1:
    pass