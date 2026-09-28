class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ls = sorted(s)
        lt = sorted(t)
        if len(ls) != len(lt):
            return False
        else:
            return ls == lt