class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        sets = {}

        for ch in s:
            sets[ch] = sets.get(ch, 0) + 1

        for ch in t:
            if ch not in sets:
                return False

            sets[ch] -= 1

            if sets[ch] < 0:
                return False

        return True