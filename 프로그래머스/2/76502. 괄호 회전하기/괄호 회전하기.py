def solution(s):
    return [check(s[i:] + s[:i]) for i in range(len(s))].count(True)
    
pairs = {')':'(', ']':'[', '}':'{'}

def check(brackets):
    stack = []
    
    for bracket in brackets:
        if bracket in '([{':
            stack.append(bracket)
        elif stack and stack[-1] == pairs[bracket]:
            stack.pop()
        else:
            return False
    return True if not stack else False
    