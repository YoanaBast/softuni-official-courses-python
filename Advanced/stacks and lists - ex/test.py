# def clock(h,m,s):
h, m, s = 7, 59, 120


if s >= 60:
    m += 1
    s = 60 - s
    if m >= 60:
        h += 1
        m = 60 - m
# return [h, m, s]



print(h, m, s)
