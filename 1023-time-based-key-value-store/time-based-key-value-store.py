from bisect import bisect_left
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
        if len(self.m[key])==1:
            return(self.m[key][0])
        x=bisect_left(self.ml[key],timestamp)
        if x>=len(self.ml[key]):
            return(self.m[key][-1])
        elif self.ml[key][x]==timestamp:
            return(self.m[key][x])
        else:
            return(self.m[key][x-1])
