from time import get_clock_info

print("time():\t\t\t", get_clock_info("time"))
print("perf_counter()\t", get_clock_info("perf_counter"))
print("monotonic():\t", get_clock_info("monotonic"))
print("process_time():\t", get_clock_info("process_time"))