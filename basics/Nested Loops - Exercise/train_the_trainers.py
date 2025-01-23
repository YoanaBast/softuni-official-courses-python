j_count = int(input())

total_sum = 0
pres_count = 0

command = input()

while command != 'Finish':
    curr_pres = command
    pres_count += 1

    curr_sum = 0

    for _ in range(j_count):
        j_score = float(input())
        curr_sum += j_score

    avg_score = curr_sum / j_count
    print(f'{curr_pres} - {avg_score:.2f}.')

    total_sum += curr_sum

    command = input()

total_avg_core = total_sum / (j_count * pres_count)
print(f'Student\'s final assessment is {total_avg_core:.2f}.')
