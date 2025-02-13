rooms_n = int(input())
total_free_chairs = 0
is_ok = True

for rooms in range(1, rooms_n + 1):
    chair_visit = input().split(' ')
    chairs = len(chair_visit[0])
    visitors = int(chair_visit[1])
    if chairs < visitors:
        diff = visitors - chairs
        print(f'{diff} more chairs needed in room {rooms}')
        is_ok = False
    else:
        diff = chairs -  visitors
        total_free_chairs += diff

if is_ok:
    print(f"Game On, {total_free_chairs} free chairs left")