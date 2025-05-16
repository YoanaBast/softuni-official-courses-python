# {[()]} - Parentheses are balanced.
# (){}[] - Parentheses are balanced.
# {[(])} - Parentheses are NOT balanced.
op_stack = []
opening = ['{', '[', '(']
closing = ['}', ']', ')']
balanced = True

par = list(input())
for p in par:
    if p in opening:
        op_stack.append(p)
    elif p in closing:
        if not op_stack: # if closing is the first one = false
            balanced = False
            break
        if closing.index(p) != opening.index(op_stack[-1]): # if closing does not match the top of the stack with opening ones
            balanced = False
            break
        op_stack.pop()

print('YES') if balanced else print('NO')