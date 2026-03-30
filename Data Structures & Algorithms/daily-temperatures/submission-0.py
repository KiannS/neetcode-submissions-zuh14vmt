class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        index = []
        res = [0 for i in range(len(temperatures))]

        for i in range(len(temperatures)):
            if len(stack) == 0:
                stack.append(temperatures[i])
                index.append(i)
                continue
            if temperatures[i] <= stack[-1]:
                stack.append(temperatures[i])
                index.append(i)
            else:
                while (stack and stack[-1] < temperatures[i]):
                    stack.pop()
                    curr = index.pop()
                    res[curr] = i - curr
                stack.append(temperatures[i])
                index.append(i)
        return res
            