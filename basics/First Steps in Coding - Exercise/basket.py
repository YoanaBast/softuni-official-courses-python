yearly_price = int(input())

shoes = yearly_price - 0.40 * yearly_price
clothes = shoes - 0.20 * shoes
ball = clothes / 4
acc = ball / 5

total = yearly_price + shoes + clothes + ball + acc
print(total)
