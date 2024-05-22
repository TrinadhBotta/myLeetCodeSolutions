from bisect import bisect_right
class TimeMap:

    def __init__(self):
        self.m = {}
        self.ml = {}
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.m:
            self.m[key]=[value]
            self.ml[key]=[timestamp]
        else:
            self.m[key].append(value)
            self.ml[key].append(timestamp)
        return

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.ml or timestamp<self.ml[key][0]:
            return('')
        x=bisect_right(self.ml[key],timestamp)
        return(self.m[key][x-1])
