class Solution:

    def isValid(self, s: str) -> bool:
        map = {

            ")": "(",
            "}": "{",
            "]": "["
        }

        if len(s) % 2 != 0:
            return False

        stack = []
        for ch in s:
            if stack and map.get(ch) == stack[-1]:
                stack.pop()
            else:
                stack.append(ch)

        return not stack


Solution().isValid("[]{}()[{})")
