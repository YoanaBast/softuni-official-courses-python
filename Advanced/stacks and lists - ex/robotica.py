from collections import deque

#ROBOTS
_robots = input().split(';')
robots_list = []
for _robot in _robots:
    name, time = _robot.split('-')
    robots_list.append({'name': name,
                   'time': int(time),
                   'av': 0})
# no need for deque in the robots, will not rotate?

#TIME
H, M, S = map(int, input().split(':'))  #8:00:00
time_seconds = H * 3600  + M * 60 + S

#ITEMS
items = deque()
while True:
    command = input()
    if command == 'End':
        break
    items.append(command)

while items:
    curr_item = items.popleft() #moved to top
    time_seconds += 1 #moved here
    is_taken = False #NEW

    for robot in robots_list:
        if robot ['av'] <= time_seconds: #NEW
            robot['av'] = time_seconds + robot['time']
            h = time_seconds // 3600
            m = (time_seconds % 3600) // 60
            s = (time_seconds % 60) % 60
            h %= 24
            curr_time = f"[{h:02d}:{m:02d}:{s:02d}]"
            print(f'{robot["name"]} - {curr_item} {curr_time}')
            is_taken = True
            break
    if not is_taken:
        items.append(curr_item)

            # 83/100
        # check https://pastebin.com/pd2guPu0