class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        time = defaultdict(int)
        res = 0 
        stack = []

        for i in range (len(position)):
            time[position[i]] = (target - position[i]) / speed[i]
        
        position.sort()

        for curr in reversed(position):
            if len(stack) == 0:
                stack.append(curr)
                res += 1
            else:
                lastCar = stack[-1]
                if time[curr] > time[lastCar]:
                    res += 1
                    stack.append(curr)
        return res







        