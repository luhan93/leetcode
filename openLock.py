class Solution:
    # important point is to count the steps.
    # 1) add marker at the end of each step.
    # 2) new queues (lists) for each step.
    def openLock(self, deadends, target) :
        deadends, visited, q, count = set(deadends), set(), ["0000"], 0
        while q:
            new = list()
            for cob in q:
                if cob == target:
                    return count
                if cob in deadends or cob in visited:
                    continue
                else:
                    visited.add(cob)
                    new.extend(self.cob_next(cob))
            q = new
            count += 1
        return -1

    def cob_next(self, cob):
        move = {str(i): [str((i + 1) % 10), str((i - 1) % 10)] for i in range(10)}
        res = []
        for i in range(len(cob)):
            res.append(cob[:i]+move[cob[i]][0]+cob[i+1:])
            res.append(cob[:i] + move[cob[i]][1] + cob[i + 1:])
        return res


x = Solution()
y = x.openLock(["0201","0101","0102","1212","2002"],"0202")
print(y)
