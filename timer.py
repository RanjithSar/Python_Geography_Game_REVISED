import time

class Timer:
    
    def __init__(self, max_time):
        self.max_time = max_time
        self.current_time = self.max_time
        
    def reset(self):
        self.current_time = self.max_time
        
    def count_down(self):
        self.current_time -= 1
        time.sleep(1)
        
    def get_time(self):
        return self.current_time