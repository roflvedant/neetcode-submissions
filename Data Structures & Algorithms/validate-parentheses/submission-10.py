class Solution:
    def isValid(self, s: str) -> bool:
        dict = {
        '}':'{',
        ']':'[',
        ')':'(',
        }

        stack = []

        for i in s:
            if i in dict: #we have to only stop when we find a closebracket therefor closed bracket is key in ddict
                if stack and stack[-1] == dict[i]:
                    stack.pop()
                else:
                    return False               
            else:
                stack.append(i)
        return True if not stack else False