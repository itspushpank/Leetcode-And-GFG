class Solution:
    def romanToInt(self, s: str) -> int:
        values = { 'I' : 1, 'V': 5, 'X':10, 'L':50 , 'C': 100, 'D': 500, 'M': 1000}
        total,prev = 0,0
        for i in reversed(s):
            cur = values[i]
            total += -cur if cur < prev else cur
            prev = cur

        return total

