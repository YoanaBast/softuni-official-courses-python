nums_stack = input().split()

#OPTION 1
nums_stack.reverse()
print(*nums_stack)

#OPTION2
rev_stack = [nums_stack.pop() for _ in range(len(nums_stack))]
print(' '.join(rev_stack))

