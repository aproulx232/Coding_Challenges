"""Implement a job scheduler which takes in a function f and an integer n, and calls f after n milliseconds."""
from threading import Thread
import time


def job_scheduler(f, n):
    delayed_start = Thread(target=_run_after_mils_thread, args=(f, n))
    delayed_start.start()
    return


def _run_after_mils_thread(f, n):
    time.sleep(n/1000)
    return f()


def test():
    print("test!")
    return


if __name__ == '__main__':
    job_scheduler(test, 1000)