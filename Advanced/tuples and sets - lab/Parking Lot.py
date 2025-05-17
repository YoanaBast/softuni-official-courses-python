n = int(input())
cars = set()
for _ in range(n):
    ac, car = input().split(', ')
    if ac == 'IN' and car not in cars:
        cars.add(car)
    elif ac == 'OUT' and car in cars:
        cars.remove(car)
if cars:
    for car in cars:
        print(car)
else:
    print('Parking Lot is Empty')