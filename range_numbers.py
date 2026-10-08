a = int(input("Введите число a: "))
b = int(input("Введите число b: "))

if a < b:
    # Шаг +1 для движения вверх
    for i in range(a, b + 1):
        print(i, end=" ")
elif a > b:
    for i in range(a, b - 1, -1):
        print(i, end=" ")
else:
    print(a)
