from collections import deque

_robots = input().split(';')
robo_q = deque()
for _robot in _robots:
    name, time = _robot.split('-')
    robo_q.append({'name': name, 'time': int(time), 'av': 0})

H, M, S = map(int, input().split(':'))  #8:00:00
time_seconds = H * 3600  + M * 60 + S

items = deque([])
while True:
    command = input()
    if command == 'End':
        break
    items.append(command)

while items:
    time_seconds += 1

    N = robo_q[0]['name']
    if robo_q[0]['av'] == 0 or robo_q[0]['av'] <= time_seconds:
        curr_item = items.popleft()
        robo_q[0]['av'] =  time_seconds
        robo_q[0]['av'] += robo_q[0]['time']
        adjusted_time = time_seconds % 86400
        h = adjusted_time // 3600
        m = (adjusted_time % 3600) // 60
        s = adjusted_time % 60
        curr_time = f"[{h:02d}:{m:02d}:{s:02d}]"
        print(f'{N} - {curr_item} {curr_time}')
        robo_q.rotate(-1)
        continue
    else:
        robo_q.rotate(-1)
        items.rotate(-1)

        # 83/100
        # check https://pastebin.com/pd2guPu0