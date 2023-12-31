import math
import matplotlib.pyplot as plt
import random


# Task 1
def rand(n, a=22695477, b=1, m=2 ** 32, x0=1):
    random_numbers = []
    x = x0

    for _ in range(n):
        x = (a * x + b) % m
        normal_number = x / m * (B - A) + A
        random_numbers.append(normal_number)

    return random_numbers


# Task 2
A = 0
B = 10

list_numbers = []

N_values = [10 ** 2, 10 ** 3, 10 ** 4, 10 ** 5]

for N in N_values:
    # random_numbers = rand(n=N)  # задание 1
    random_numbers = [random.uniform(A, B) for _ in range(N)]  # задание 7
    list_numbers.append(random_numbers)

# № вывод последовательностей
# for idx, random_numbers in enumerate(list_numbers):
#    print(f'N={N_values[idx]}: Интервал [{random_numbers}]')


# Task 3
def mat_wait(random_numbers):
    return sum(random_numbers) / len(random_numbers)

def dispers(random_numbers, mean):
    return sum((x - mean) ** 2 for x in random_numbers) / (len(random_numbers) - 1)

theor_mat = (A + B) / 2
theor_dispers = (B - A) ** 2 / 12
print(f'Теоретическое математическое ожидание: {theor_mat}')
print(f'Теоретическая дисперсия: {theor_dispers}')

for idx, N in enumerate(N_values):
    random_numbers = list_numbers[idx]
    mat_value = mat_wait(random_numbers)
    dispers_value = dispers(random_numbers, mat_value)

    error_mat = abs((mat_value - theor_mat) / theor_mat) * 100
    error_dispers = abs((dispers_value - theor_dispers) / theor_dispers) * 100

    print(f'N={N}:')
    print(f'  Математическое ожидание: {mat_value}, Погрешность: {error_mat}')
    print(f'  Дисперсия: {dispers_value}, Погрешность: {error_dispers}')
    print('------------------------------')

#task 4
def rand_period(random_numbers):
    n = len(random_numbers)
    period = 0
    first_pos = 1
    second_pos = 2

    for i in range(n):
        element = random_numbers[i]
        for j in range(i, n):
            if element == random_numbers[j] and i != j:
                period = j - i
                first_pos = i
                second_pos = j
                return period, first_pos, second_pos

    period = -1
    first_pos = -1
    second_pos = -1
    return period, first_pos, second_pos


for idx, random_numbers in enumerate(list_numbers):
    period, first_pos, second_pos = rand_period(random_numbers)
    print(f'Период: {period}, Первое вхождение: {first_pos}, Второе вхождение: {second_pos}')

#Task 5-6

def get_freq_distr(X, A, B, IntervalsCount, dY):
    Freq = [0] * IntervalsCount

    for Yc in X:
        fN = math.floor((Yc - A) / dY)
        if fN == IntervalsCount:
            fN -= 1
        Freq[fN] += 1

    for i in range(IntervalsCount):
        Freq[i] = Freq[i] / (len(X) * dY)

    x_values = [A + (dY * (0.5 + i)) for i in range(IntervalsCount)]

    return x_values, Freq


for idx, N in enumerate(N_values):
    random_numbers = list_numbers[idx]
    dY = (10 - 0) / 10
    x_values, frequencies = get_freq_distr(random_numbers, 0, 10, 10, dY)

    plt.bar(x_values, frequencies, width=dY, align='edge')
    plt.xlabel('Интервалы')
    plt.ylabel('Относительные частоты')
    plt.title(f'Гистограмма для N={N}')
    plt.show()

    Pearson = 0
    for k in range(len(frequencies)):
        Pearson += (1 / 10 - frequencies[k]) ** 2 / frequencies[k]
    print(f'Значение критерия Пирсона для N={N}: {Pearson}')


