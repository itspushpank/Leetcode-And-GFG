class Solution:
    def isValid(self,s: str) -> bool:
        stack = []
        flag = {')':'(',']':'[','}':'{'}
        for i in s:
            if i in flag:
                if not stack or stack[-1] != flag[i]:
                    return False
                stack.pop()
            else:
                stack.append(i)
        return not stack