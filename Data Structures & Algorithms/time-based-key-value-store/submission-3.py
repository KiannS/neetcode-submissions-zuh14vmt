class TimeMap:

    def __init__(self):
        self.map = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
            self.map[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if not key in self.map:
            return ""
        
        time = self.map[key][0][0]

        if timestamp < time:
            return ""
        if timestamp > self.map[key][-1][0]:
            return self.map[key][-1][1]

        else:
            return self.search(key, timestamp)

    def search(self, key: str, timestamp: int) -> str:
        values = self.map[key]
        l = 0
        r = len(values) - 1

        while l <= r:
            mid = (l+r)//2
            time, val = values[mid]

            if time == timestamp:
                return val
            elif time > timestamp:
                r = mid - 1
            else:
                l = mid + 1

        return values[r][1]

