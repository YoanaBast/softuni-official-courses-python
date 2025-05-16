from collections import deque
pumps_n = int(input())
pumps = deque()

for pump in range(pumps_n): # 0 1 2 3
    fuel, distance = input().split()
    pumps.append({"fuel": int(fuel), "distance": int(distance)})
start = 0
stops = 0

while stops < pumps_n:
    fuel = 0
    for i in range(pumps_n): # 0 1 2
        fuel += pumps[i]['fuel']
        distance = pumps[i]['distance']
        if fuel < distance:
            pumps.rotate(-1)
            start += 1
            stops = 0
            break
        fuel -= distance
        stops += 1

print(start)
