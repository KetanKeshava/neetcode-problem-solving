class Solution:
    def isValid(self, s: str) -> bool:
        stack = list()

        for bracket in s:
            if bracket in ['(', '{', '[']:
                stack.append(bracket)
            elif bracket == ')':
                if len(stack) and stack[-1] == '(':
                    stack.pop()
                else:
                    return False

            elif bracket == ']':
                if len(stack) and stack[-1] == '[':
                    stack.pop()
                else:
                    return False

            elif bracket == '}':
                if len(stack) and stack[-1] == '{':
                    stack.pop()
                else:
                    return False


        return (len(stack) == 0)
            