n = int(input('Введите количество монеток:'))
count_zero = 0
count_one = 0
for i in range(n):
    x = int(input('Введите 0 или 1:'))
    if x == 0:
        count_zero += 1
    else:
        count_one += 1
if count_one > count_zero:
    print(count_zero)3
else:
    print(count_one)
