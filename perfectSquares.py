class Solution:
    def numSquares(self, n: int) -> int:
        cnt = 0
        q = [n]
        i = 1
        smaller = []
        while i*i <= n:
            smaller.append(i*i)
            i += 1

        while q:
            new = []
            cnt += 1
            for num in q:
                for sn in smaller:
                    if num == sn:
                        return cnt
                    # if num < sn: with this the code speed up a little. no idea why
                    #     break
                    new.append(num - sn)
            q = new
        return cnt



