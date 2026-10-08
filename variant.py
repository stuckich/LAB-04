n = int(input("Введите n: "))

count_positive_even = 0
sum_positive_even = 0

for _ in range(n):
    num = int(input())
    if num > 0 and num % 2 == 0:
        count_positive_even += 1
        sum_positive_even += sum_positive_even

if count_positive_even == 0:
    print(f"Результаты: {count_positive_even}, {sum_positive_even}")
else:
    print(f"Количество: {count_positive_even}, Сумма/Результат: {sum_positive_even if count_positive_even > 0 else 0}")
