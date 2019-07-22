class Solution:
    def countAndSay(self, n: int) -> str:
        res = "1"
        i = 1
        while i < n:
            num = res[0]
            l = 1
            temp = ""
            for j in range(1,len(res)):
                if res[j] == res[j-1]:
                    l = l+1
                else:
                    temp = temp + str(l) + num
                    l = 1
                    nums = res[j]
            res = temp
            i = i+1
        return res

