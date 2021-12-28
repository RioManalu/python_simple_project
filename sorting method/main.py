a = [5, 10, 2, 7, 3, 9]


def urutkan(num):
    for i in range(len(num) - 1, 0, -1):
        for j in range(i):
            if num[j] > num[j + 1]:
                num[j], num[j + 1] = num[j + 1], num[j]


urutkan(a)
print(a)
