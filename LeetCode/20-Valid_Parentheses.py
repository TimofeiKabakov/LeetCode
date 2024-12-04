class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if char == '(' or char == '{' or char == '[':
                stack.append(char)
            elif len(stack) and (stack[-1] == '(' and char == ')' or stack[-1] == '{' and char == '}' or stack[-1] == '[' and char == ']'):
                stack.pop()
            else:
                return False
                
        return not len(stack)

# Time Complexity: O(n)
# Space Complexity: O(n)