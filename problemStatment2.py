"""
Problem Statement 2: MultiThreading
● Write a python code to do the following:
○ It should be able to launch 3 different thread
○ Each thread should print this every 5 second:
■ Thread <thread number> is running at <time elapsed>
■ E.g.
● "Thread 2 is running at 0"
● "Thread 2 is running at 5"
● "Thread 2 is running at 10"
○ Initially start thread 1 and 3
○ After 20 second stop thread 1 start thread 2
○ Again after 18 second stop thread 3 and start thread 1
"""

# importing the required library threading and time
import threading
import time


# creating a child class of threading to replicate the pause and resume functionality
class CreateThread(threading.Thread):

    # initializing our class with:-
    #     1. initializing the parent class thread by super keyword
    #     2. thread_number variable for keeping track of thread
    #     3. flag variable to replicate a pause/resume switch for our thread running
    #     4. clock variable to keep track of time
    def __init__(self, thread_number):
        super().__init__()
        self.thread_number = thread_number
        self.flag = True
        self.clock = 0

    # pause function which will act like a switch to pause the thread output on screen
    def pause(self):
        self.flag = False

    # resume function which will act like a switch to resume the thread output from where it was paused
    def resume(self):
        self.flag = True
        self.run()

    # run function is taken as the default target function by the threads
    def run(self):

        # on the basis of flag variable we initiated this will fed output to screen
        while self.flag:

            # on every 5 second basis printing the output to screen
            if self.clock % 5 == 0:
                print(f"Thread {self.thread_number} is running at {self.clock}  ")

            time.sleep(1)
            self.clock += 1


def problem_statement_2():

    # creating objects of our class
    thread_1 = CreateThread(1)
    thread_2 = CreateThread(2)
    thread_3 = CreateThread(3)

    # initializing our required thread 1 and 3
    thread_1.start()
    thread_3.start()

    # providing 20 seconds of wait/sleep before pausing our thread 1 and starting thread 2
    time.sleep(20)
    thread_1.pause()
    thread_2.start()

    # providing 18 seconds of wait/sleep before pausing our thread 3 and resuming thread 1
    time.sleep(18)
    thread_3.pause()
    thread_1.resume()


# function to initialize our required setup of threads
problem_statement_2()
