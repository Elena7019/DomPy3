# 5) Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
def fib(n):
    if n in [1, 2]:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


def fibN(n):
    if n == 1:
        return 1
    elif n == 2:
        return -1
    else:
        f1, f2 = 1, -1
        for i in range(2, n):
            f1, f2 = f2, f1 - f2
        return f2


list = [0]
a = int(input('Задайте число: '))
for j in range(1, a + 1):
    list.append(fib(j))
    list.insert(0, fibN(j))
print(list)
