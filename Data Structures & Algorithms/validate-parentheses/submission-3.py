class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if char == '(' or char == '{' or char == '[':
                stack.append(char)
                continue
            

            if char == ')' :
                if len(stack) <=0 :
                    openingchar = None
                else:
                    openingchar = stack.pop()
                if openingchar != '(':
                    return False
            elif char == '}':
                if len(stack) <=0 :
                    openingchar = None
                else:
                    openingchar = stack.pop()
                if openingchar != '{':
                    return False
            elif char == ']':
                if len(stack) <=0 :
                    openingchar = None
                else:
                    openingchar = stack.pop()
                if openingchar != '[':
                    return False
        if len(stack) != 0:
            return False
        return True

        