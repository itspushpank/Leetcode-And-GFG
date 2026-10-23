class Solution:
    def isValid(self,s: str) -> bool:
        stack = []
        flag = {')':'(',']':'[','}':'{'}
        for i in s:
            if i in "([{":
                stack.append(i)
                print(i)

            elif i in "}])" and len(stack) != 0 and flag[i] == stack[-1]:
                print(stack.pop())
            else:
                return False

        if len(stack) == 0:
            return True
        return False
        