a,b,c = [int(x) for x in input('date 1: ').split()]

d,e,f = [int(x) for x in input('date 2: ').split()]

day = abs(d - a)
month = abs(e - b)
year = abs(f-c)

print(f'{year} year {month} month {day} day')
