"""Задание номер №3"""


from sys import *
setrecursionlimit(2500)

def lkm(i, x_n, p, out_list):
    if i == 0:
        return x_n

    m = 31104
    a = 625
    c = 6571

    x_n_next = (a * x_n + c) % m

    znach = x_n_next / m
    if znach < p:
        out_list.append(0)
    else:
        out_list.append(1)

    i = i - 1

    return lkm(i, x_n_next, p, out_list)

A_choices = []
x_current = lkm(100, 7, 0.5, A_choices)

B_choices = []
lkm(100, x_current, 0.25, B_choices)

res = list(zip(A_choices, B_choices))


#2).
print("\n2).")

c_00, c_11 = res.count((0, 0)), res.count((1, 1))
c_01, c_10 = res.count((0, 1)), res.count((1, 0))

a_v1 = c_00 * 3
a_v2 = c_11 * 5
b_v1 = c_01 * (-2)
b_v2 = c_10 * (-5)

experiment_mean = (a_v1 + a_v2 + b_v1 + b_v2) / 100

print(f"Суммарный выигрыш игрока А\n"
      f"в проведенном эксперименте "
      f"= {a_v1 + a_v2 + b_v1 + b_v2}\n")
print(f"Суммарный выигрыш игрока B\n"
      f"в проведенном эксперименте "
      f"= {(-1) * (a_v1 + a_v2 + b_v1 + b_v2)}\n")

print(f"Среднее экспериментальное "
      f"значение выигрыша игрока "
      f"A\nв проведенном эксперимен"
      f"те = {experiment_mean}\n")
print(f"Среднее экспериментальное "
      f"значение выигрыша игрока "
      f"B\nв проведенном эксперимен"
      f"те = {(-1) * experiment_mean}")


#3).
print("\n3).")

E = (3 * 0.125 + (-2) * 0.375 +
         (-5) * 0.125 + 5 * 0.375)
print(f"Математическое ожидание среднего значения\n"
      f"выигрыша игрока A "
      f" (теоретическая оценка выигрыша) = {E}\n")
print(f"Математическое ожидание среднего значения\n"
      f"выигрыша игрока B "
      f" (теоретическая оценка выигрыша) = {(-1) * E}")


#4).
print("\n4).")

sr_kv_otkl_ex_s = (c_00 * (3 - experiment_mean)**2 +
    c_11 * (5 - experiment_mean)**2 +
    c_01 * ((-2) - experiment_mean)**2 +
    c_10 * ((-5) - experiment_mean)**2)

sr_kv_otkl_ex = (sr_kv_otkl_ex_s / 100) ** 0.5

print(f"Среднее квадратичное отклонение от \nэкспериментального среднего = {sr_kv_otkl_ex}")


#5).
print("\n5).")

E_xkv = (3**2 * 0.125 + (-2)**2 * 0.375 +
         (-5)**2 * 0.125 + 5**2 * 0.375)

D = E_xkv - E ** 2
sr_kv_otkl_teor = D ** 0.5

print(f"Дисперсия = {D}\n")

print(f"Теоретическое среднее\nквадратичное "
      f"отклонение = {sr_kv_otkl_teor}")
