budget = float(input())
video_count = int(input())
pro_count = int(input())
ram_count = int(input())

vid_price = 250
proc_price = 0.35 * vid_price*video_count
ram_price = 0.10 * vid_price*video_count

total = vid_price*video_count + proc_price*pro_count + ram_price*ram_count

if video_count > pro_count:
    total = 0.85 * total

if budget >= total:
    print(f"You have {budget - total:.2f} leva left!")

else:
    print(f"Not enough money! You need {total - budget:.2f} leva more!")

    # if video_count > pro_count:
    #     total = 0.85 * total
    #
    #     if budget >= total:
    #         print(f"You have {budget - total:.2f} leva left!")
    #
    #     else:
    #         print(f"Not enough money! You need {total - budget:.2f} leva more!")