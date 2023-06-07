#Задача 28

a = int(input("Введите первое неотрицительное число "))
b = int(input("Введите второе неотрицательно число "))
def r_sum(a, b):
    if a == 0:
        return b
    else:
        return r_sum(a - 1, b + 1)
print(r_sum(a, b))