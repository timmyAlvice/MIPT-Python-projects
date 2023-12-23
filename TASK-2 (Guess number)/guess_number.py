"""
Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np


def binary_predict(number: int = 1) -> int:
    """Предсказывает число за счёт алгоритма бинарного поиска


    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: к-во итераций (попыток)
    """
    # счётчик попыток
    count = 0
    # значение предсказания загаданного числа
    # и шаг сокращения разброса значений
    step = predict = 50
    
    # цикл, пока выполняется условие: 
    # "предсказание не равно истинноому значению"
    
    while number != predict:
        # счётчик увеличивается на 1 на каждой итерции цикла
        count += 1
        # шаг сокращения делим на 2, пока он не равен 1,
        # иначе делим на 1
        step //= 2 if step != 1 else 1
        # если истинное значение меньше предсказания,
        # значение предсказания уменьшается на значение шага
        if number < predict:
            predict -= step
        # если больше, увеличивается соответственно
        elif number > predict:
            predict += step
            
    # цикл прирвётся автоматически, 
    # когда значение предсказание сравняется с истинным
    # возращается значение счётчика попыток
    return count


def score_game(predict_func) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    #np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел

    for number in random_array:
        count_ls.append(predict_func(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за: {score} попыток")
    return score


if __name__ == "__main__":
    # RUN
    score_game(binary_predict)
