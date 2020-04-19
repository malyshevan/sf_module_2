# -*- coding: utf-8 -*-
import numpy as np


def score_game(game_core_v1):
    '''Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число'''
    count_ls = []
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(1, 101, size=(1000))
    for number in random_array:
        count_ls.append(game_core_v1(number))
       #print(count_ls)
    score = int(np.mean(count_ls))
    
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return(score)
    
def game_core_v2(number):
    '''Сначала устанавливаем любое random число, а потом уменьшаем или увеличиваем его в зависимости от того, больше оно или меньше нужного.
       Функция принимает загаданное число и возвращает число попыток'''
    count = 0
    predict = np.random.randint(1,100)
    #print('num', number)
    while number != predict:
        count+=1
        if number > predict and number > predict + 10: 
            predict += 10
        elif number > predict:
            predict += 1   
        elif number < predict and number < predict - 10:
            predict -= 10
        elif number < predict:
            predict -= 1            
        #print('pred', predict)
    
    return(count) # выход из цикла, если угадали

# Проверяем
score_game(game_core_v2)