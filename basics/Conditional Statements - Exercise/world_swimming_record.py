rec_to_beat_sec = float(input())
distance_meters = float(input())
time_per1m_sec = float(input())

from math import floor
debuff = floor(distance_meters / 15) * 12.5
total_ivan = distance_meters * time_per1m_sec + (debuff)

if total_ivan < rec_to_beat_sec:
    print(f" Yes, he succeeded! The new world record is {total_ivan:.2f} seconds.")

else:
    print(f"No, he failed! He was {total_ivan - rec_to_beat_sec:.2f} seconds slower.")

