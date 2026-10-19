class TimeMap:

    def __init__(self):
        # time based key vaue data structure
        # strore multiple values for the same key, at different time stamps. 
        self.struct = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.struct:
            self.struct[key].append((value, timestamp))
        else:
            self.struct[key] = [(value, timestamp)]

        

    def get(self, key: str, timestamp: int) -> str:
        output = ""
        if not key in self.struct:
            return output

        lo, hi = 0, len(self.struct[key]) - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            if self.struct[key][mid][1] <= timestamp:
                output = self.struct[key][mid][0]   # valid candidate, try for a later one
                lo = mid + 1
            else:
                hi = mid - 1
        return output


        
