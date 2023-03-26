fires = {'a': 0, 'b' : 0, 'c' : 0}
total = 0

def getMinimumPressCount(self, other):
    a = abs(self - other)
    b = 10 - a
    return min(a, b)

n = int(input())

numbers = map(int, input().split())
for num in numbers:
    count_a = getMinimumPressCount(fires['a'], num)
    count_b = getMinimumPressCount(fires['b'], num)
    count_c = getMinimumPressCount(fires['c'], num)
    min_press = min(count_a, count_b, count_c)

    which_fire = None
    if min_press == count_a:
        which_fire = 'a'
    elif min_press == count_b:
        which_fire = 'b'
    else:
        which_fire = 'c'

    fires[which_fire] = num
    total += min_press

print(total)

    