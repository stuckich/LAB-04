rejected_count = 0

while True:
    num = int(input("Введите положительное число: "))
    
    if num > 0:
        break
    else:
        rejected_count += 1

squared = num ** 2

print(f"Квадрат числа: {squared}")
print(f"Количество отклонённых вводов: {rejected_count}")
