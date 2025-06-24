from datetime import time, datetime

class FileLog:
    def clear_the_log(self):
        # Simulated method that would do something to files in the log
        print("Log cleared")  # Optional: simulate activity

class DataClerk:
    def __init__(self, file_log):
        self._file_log = file_log

    def process_data(self):
        now = datetime.now().time()
        stop_time = time(20, 0)  # 20:00 in 24-hour format

        if now < stop_time:
            print("Ready to process the data")
            self._file_log.clear_the_log()

