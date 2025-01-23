ser_name = str(input())
ep_len = int(input())
break_dur = int(input())

food = 1/8 * break_dur
rest = 1/4 * break_dur
from math import ceil

if ep_len <= break_dur - food - rest:
    print(f"You have enough time to watch {ser_name} and left with {ceil(break_dur - food - rest - ep_len)} minutes free time.")

else:
    print(f"You don't have enough time to watch {ser_name}, you need {ceil((break_dur - food - rest - ep_len) *-1)} more minutes.")
