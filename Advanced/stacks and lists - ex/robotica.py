from collections import deque

def clock(h,m,s):
    s += 1
    if s == 60:
        m += 1
        s = 0
        if m >= 60:
            h += 1
            m = 60 - m
    return [h, m, s]

_robots = input().split(';')
robo_q = deque()
for _robot in _robots:
    name, time = _robot.split('-')
    robo_q.append({'name': name, 'time': int(time), 'av': 0, 'ex': 0})

H, M, S = map(int, input().split(':'))  #8:00:00

items = deque([])
while True:
    command = input()
    if command == 'End':
        break
    items.append(command)

while items:
    for r in range(len(robo_q)):
        if robo_q[r]['av'] > 0:
            robo_q[r]['av'] -= 1
            robo_q[r]['ex'] += 1



    if robo_q[0]['av'] == 0:
        S += robo_q[0]['ex']
        H, M, S = clock(H, M, S)
        time = f'[{H}:{M}:{S}]'

        print(f'{robo_q[0]['name']} - {items[0]} - {time}')
        items.popleft()
        robo_q[0]['av'] = robo_q[0]['time']

    robo_q.rotate(-1)
