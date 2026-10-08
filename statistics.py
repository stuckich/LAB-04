n = int(input("Введите количество чисел (n >= 1): "))

first_num = int(input("Введите число: "))
minimum = first_num
maximum = first_num
total_sum = first_num

for _ in range(n - 1):
    num = int(input("Введите число: "))
    total_sum += num
    
    if num < minimum:
        minimum = num
    if num > maximum:
        maximum = num

average = total_sum / n

print(f"Минимум: {minimum}")
print(f"Максимум: {maximum}")
print(f"Среднее значение: {average}")
