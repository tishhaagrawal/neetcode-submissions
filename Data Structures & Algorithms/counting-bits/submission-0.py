class Solution:
    def countBits(self, n: int) -> List[int]:
        arr = [0]*(n+1)
        for i in range (len(arr)):
            num = i
            res = 0
            while num:
                num &= (num -1)
                res +=1
            arr[i] = res
        return arr


        