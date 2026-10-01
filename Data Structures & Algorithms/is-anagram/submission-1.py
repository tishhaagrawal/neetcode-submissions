class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        my_map = defaultdict(int)
        for i in range(len(s)):
            my_map[s[i]] += 1
            my_map[t[i]] -=1 
        if all(value ==0 for value in my_map.values()): return True
        return False
        