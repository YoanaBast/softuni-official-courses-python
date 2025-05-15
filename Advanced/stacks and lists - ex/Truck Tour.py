from collections import deque
pumps_n = int(input())
pumps = deque([])
for pump in range(pumps_n):
    pumps.append([int(x) for x in input().split()])
fuel = 0
popped = {}
station = -1
while pumps and len(popped) < pumps_n:
    station += 1
    fuel += pumps[0][0]
    distance = pumps[0][1]
    pumps.rotate(pumps_n - 1)
    if fuel >= distance:
        fuel -= distance
        popped[station] = pumps.pop()

result = list(popped.keys())[0] #access first key
print(result)