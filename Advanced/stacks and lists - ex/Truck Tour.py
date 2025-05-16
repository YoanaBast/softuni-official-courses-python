from collections import deque
pumps_n = int(input())
pumps = deque()

for pump in range(pumps_n):
    fuel, distance = input().split()
    pumps.append({pump: {"fuel": int(fuel), "distance": int(distance)}})

start = 0
stops = -1

while stops < pumps_n:
    fuel = 0
    for i in range(pumps_n):
        fuel += pumps[0]['fuel']
        distance = pumps[0]