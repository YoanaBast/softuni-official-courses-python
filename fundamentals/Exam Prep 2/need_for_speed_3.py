num_cars = int(input())
cars = {}
for _ in range(num_cars):
    car, mileage, fuel = input().split('|')  #  "{car}|{mileage}|{fuel}"
    cars[car] = [mileage, fuel]


command = input().split(" : ")
while True:
    if command[0] == 'Stop':
        for car in cars.keys():
            mileage, fuel = cars[car][0], cars[car][1]
            print(f"{car} -> Mileage: {mileage} kms, Fuel in the tank: {fuel} lt.")
        break
#  DRIVE
    elif command[0] == 'Drive':  # "Drive : {car} : {distance} : {fuel}":
        car, distance, fuel_needed = command[1], int(command[2]), int(command[3])
        current_mil, available_fuel = int(cars[car][0]), int(cars[car][1])
        if available_fuel < fuel_needed:
            print("Not enough fuel to make that ride")
        else:
            cars[car][1] = available_fuel = available_fuel - fuel_needed
            cars[car][0] = current_mil = current_mil + distance
            print(f"{car} driven for {distance} kilometers. {fuel_needed} liters of fuel consumed.")

        if current_mil >= 100_000:
            cars.pop(car)
            print(f"Time to sell the {car}!")

#  REFUEL, Each tank can hold a maximum of 75 liters of fuel
    elif command[0] == 'Refuel':  # "Refuel : {car} : {fuel}":
        car, fuel_added = command[1], int(command[2])
        available_fuel = int(cars[car][1])
        if available_fuel + fuel_added > 75:
            fuel_added = 75 - available_fuel
            cars[car][1] = available_fuel = 75
        else:
            available_fuel += fuel_added
            cars[car][1] = available_fuel
        print(f"{car} refueled with {fuel_added} liters")
# REVERT
    elif command[0] == 'Revert':  # "Revert : {car} : {kilometers}":
        car, kilometers = command[1], int(command[2])
        current_mil = int(cars[car][0])
        if current_mil - kilometers < 10_000:
            cars[car][0] = current_mil = 10_000
        else:
            current_mil -= kilometers
            cars[car][0] = current_mil
            print(f"{car} mileage decreased by {kilometers} kilometers")

    command = input().split(" : ")
