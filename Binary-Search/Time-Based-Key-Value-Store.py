class TimeMap:

    def __init__(self):

        # Store user:[] pairs where the list is in ascending order of timestamps
        self.users = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        
        # Update the user dictionary with the timestamp, or create a new user with one
        if not key in self.users:
            self.users.update({key:[[timestamp, value]]})
        else:
            self.users[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        
        if not key in self.users: return ""

        # Use binary search to try to find the closest timestamp value
        timestamps = self.users[key]
        l, r = 0, len(timestamps) - 1

        while l <= r:

            middle = int((l + r) / 2)
            guess = timestamps[middle][0]

            if guess == timestamp:
                return timestamps[middle][1]
            
            if guess < timestamp:
                l = middle + 1

            else:
                r = middle - 1

        # Use logic based on the contraints given in the problem to return the correct
        # timestamp that is based on the closest index found from binary search
        if middle == 0 and timestamps[middle][0] < timestamp: return timestamps[middle][1]
        elif middle > 0 and timestamps[middle][0] < timestamp: return timestamps[middle][1]
        elif middle > 0 and timestamps[middle][0] > timestamp: return timestamps[middle-1][1]
        else: return ""