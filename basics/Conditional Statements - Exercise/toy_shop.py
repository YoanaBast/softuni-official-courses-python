Price_jsw = 2.60
Price_spd = 3
Price_stb = 4.10
Price_min = 8.20
Price_truck = 2

ex_cost = float(input())

jsw_count = int(input())
spd_count = int(input())
stb_count = int(input())
min_count = int(input())
truck_count = int(input())

earnings = (jsw_count * Price_jsw) + (spd_count * Price_spd) + (stb_count * Price_stb) + (min_count * Price_min) + \
           (truck_count * Price_truck)
discount = 0
if jsw_count + spd_count + stb_count + min_count + truck_count >= 50:
    discount = earnings * 0.25

rent = (earnings - discount) * 0.10

can_we_go = earnings - ex_cost - rent - discount

if can_we_go >= 0:
    print(f"Yes! {can_we_go:.2f} lv left.")

elif can_we_go < 0:
    can_we_go = can_we_go * -1
    print(f"Not enough money! {(can_we_go):.2f} lv needed.")
