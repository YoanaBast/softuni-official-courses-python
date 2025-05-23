total_tickets = 0
total_student, total_standard,total_kid = 0, 0, 0
command = input()
while command != 'Finish':  # 'Finish' or current_movie
    current_movie = command

    # На втори ред – свободните места в салона за всяка прожекция
    seats_available = int(input())
    total_seat = seats_available

    # За всеки филм, се чете по един ред до изчерпване на свободните места
    # или до получаване на командата "End":
    # o Типа на закупения билет – текст ("student", "standard", "kid")
    ticket = input()  # 'End' or ticket_type ("student", "standard", "kid")
    while ticket != 'End':
       if ticket == 'student':
           total_student += 1
       elif ticket == 'standard':
           total_standard += 1
       elif ticket == 'kid':
           total_kid += 1

       seats_available -= 1
       if seats_available <= 0:
            break

        ticket = input()

    seats_bought = total_seat - seats_available
    percent_full = seats_bought / total_seat * 100
    print(f'{current_movie} - {percent_full:.2f}% full.')

    total_tickets += seats_bought

    command = input()
student_percent = total_student / total_tickets * 100
standard_percent = total_standard / total_tickets * 100
kid_percent =  total_kid / total_tickets * 100

print(f"Total tickets: {total_tickets}")
print(f"{student_percent:.2f}% student tickets.")
print(f"{standard_percent:.2f}% standard tickets.")
print(f"{kid_percent:.2f}% kids tickets.")

total_tickets = 0
total_student, total_standard, total_kid = 0, 0, 0

command = input()
while command != 'Finish':  # 'Finish' or current_movie
    current_movie = command

    # On the second line – available seats in the theater for each screening
    seats_available = int(input())
    total_seat = seats_available

    # For each movie, read one line until seats are filled or command "End" is received:
    ticket = input()  # 'End' or ticket_type ("student", "standard", "kid")
    while ticket != 'End':
        if ticket == 'student':
            total_student += 1
        elif ticket == 'standard':
            total_standard += 1
        elif ticket == 'kid':
            total_kid += 1

        seats_available -= 1
        if seats_available <= 0:
            break

        ticket = input()  # Read next ticket or "End"

    seats_bought = total_seat - seats_available
    percent_full = seats_bought / total_seat * 100
    print(f'{current_movie} - {percent_full:.2f}% full.')

    total_tickets += seats_bought

    command = input()

if total_tickets > 0:  # Prevent division by zero
    student_percent = total_student / total_tickets * 100
    standard_percent = total_standard / total_tickets * 100
    kid_percent = total_kid / total_tickets * 100

    print(f"Total tickets: {total_tickets}")
    print(f"{student_percent:.2f}% student tickets.")
    print(f"{standard_percent:.2f}% standard tickets.")
    print(f"{kid_percent:.2f}% kids tickets.")