from ssg import hooks
import time


start_time = None
total_written = 0


@hooks.register("start_build")
def start_build():
    global start_time
    start_time = time.time()


@hooks.register("stats")
def written():
    global total_written
    total_written += 1

    