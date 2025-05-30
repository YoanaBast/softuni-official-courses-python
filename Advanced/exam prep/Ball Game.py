from collections import deque
goals = 0
strength = deque([int(x) for x in input().split()])
accuracy = deque([int(x) for x in input().split()])

while strength and accuracy:
    last_str = strength.pop()
    first_a = accuracy.popleft()
    sumi = last_str + first_a
    if sumi == 100:
        goals += 1

    elif sumi < 100:
        if last_str < first_a:
            accuracy.appendleft(first_a)
        elif first_a < last_str:
            strength.append(last_str)

        elif last_str == first_a:
            strength.append(sumi)

    elif sumi > 100:
        strength.append(last_str - 10)
        accuracy.append(first_a)

    elif sumi > 100:
        strength.append(last_str - 10)
        accuracy.append(first_a)


if goals == 3:
    print("Paul scored a hat-trick!")

elif goals == 0:
    print("Paul failed to score a single goal.")

elif goals > 3:
    print("Paul performed remarkably well!")

elif 0 <  goals < 3:
    print("Paul failed to make a hat-trick.")
if goals > 0:
    print(f"Goals scored: {goals}")

if strength:
    print(f"Strength values left: {', '.join(map(str, strength))}")

if accuracy:
    print(f"Accuracy values left: {', '.join(map(str, accuracy))}")

#my logc was all correct, i had a typo in if accuracy: Strength values from copy paste