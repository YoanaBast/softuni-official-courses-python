hapiness = list(map(int, input().split(' ')))
impv_factor = int(input())

mult = list(map(lambda x: x * impv_factor, hapiness))

average = sum(mult) / len(mult)
happy_ppl = list(filter(lambda a: a >= average, mult))

if len(happy_ppl) < len(mult) / 2:
    print(f"Score: {len(happy_ppl)}/{len(mult)}. Employees are not happy!")
else:
    print(f"Score: {len(happy_ppl)}/{len(mult)}. Employees are happy!")

