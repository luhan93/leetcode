class Solution:
    def dailyTemperatures(self, T):
        days = [0]*len(T)
        stack = []
        for i in range(len(T)):
            while stack and T[i] > T[stack[-1]]:
                d = stack[-1]
                days[d] = i-stack.pop(-1)
            stack.append(i)
        return days


x = Solution()
print(x.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))
