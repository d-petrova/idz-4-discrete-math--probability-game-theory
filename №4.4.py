"""Задание номер №4.4"""


from sys import *
setrecursionlimit(2500)

x0 = 7

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


# Обучение (1000 игр)
red_A = 1000
blue_A = 1000
red_B = 1000
blue_B = 1000
x_state = x0

for game in range(1000):
    if red_A + blue_A == 0:
        p_A = 0.5
    else:
        p_A = red_A / (red_A + blue_A)

    if red_B + blue_B == 0:
        p_B = 0.5
    else:
        p_B = red_B / (red_B + blue_B)

    tmp_A = []
    x_state = lkm(1, x_state, p_A, tmp_A)
    choice_A = tmp_A[0]

    tmp_B = []
    x_state = lkm(1, x_state, p_B, tmp_B)
    choice_B = tmp_B[0]

    if choice_A == 0 and choice_B == 0:
        win = 3
    elif choice_A == 0 and choice_B == 1:
        win = -2
    elif choice_A == 1 and choice_B == 0:
        win = -5
    else:
        win = 5

    if win > 0:
        # A выиграл → A добавляет, B удаляет
        if choice_A == 0:
            red_A += win
        else:
            blue_A += win

        if choice_B == 0:
            red_B -= win
        else:
            blue_B -= win
    elif win < 0:
        if choice_A == 0:
            red_A += win
        else:
            blue_A += win

        if choice_B == 0:
            red_B -= win
        else:
            blue_B -= win

    red_A = max(0, red_A)
    blue_A = max(0, blue_A)
    red_B = max(0, red_B)
    blue_B = max(0, blue_B)

final_p_A = red_A / (red_A + blue_A)
final_p_B = red_B / (red_B + blue_B)

print(f"После 1000 игр обучения:")
print(f"  A: красных = {red_A}, синих = {blue_A}, p_A = {final_p_A}")
print(f"  B: красных = {red_B}, синих = {blue_B}, p_B = {final_p_B}\n")


# Контрольный эксперимент (100 игр) с полученными вероятностями final_p_A и final_p_B

A_choices = []
B_choices = []

x_state = lkm(100, x_state, final_p_A, A_choices)
x_state = lkm(100, x_state, final_p_B, B_choices)

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

E = (3 * final_p_A * final_p_B +
    (-2) * final_p_A * (1 - final_p_B) +
    (-5) * (1 - final_p_A) * final_p_B +
    5 * (1 - final_p_A) * (1 - final_p_B))

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

E_xkv = (3**2 * (final_p_A * final_p_B) +
         (-2)**2 * (final_p_A * (1 - final_p_B)) +
         (-5)**2 * ((1 - final_p_A) * final_p_B) +
         5**2 * ((1 - final_p_A) * (1 - final_p_B)))

D = E_xkv - E ** 2
sr_kv_otkl_teor = D ** 0.5

print(f"Дисперсия = {D}\n")

print(f"Теоретическое среднее\nквадратичное "
      f"отклонение = {sr_kv_otkl_teor}")
