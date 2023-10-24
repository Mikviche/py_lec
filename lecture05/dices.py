import itertools as it
import re

# проверка корректности ввода
def check(a):
    if re.fullmatch(r'\d{0,2}d\d{1,}',a): # проверяет полное совпадение с шаблонной строкой: от нуля до двух цифр, d, не менее одной цифры
        return True 
    return False

# Конвертация в список, удобный для работы
def convert(a):
    dice = a.split("d")                                        # делю строку по d
    b = []                                                     # делаю массив, который заполню как [число бросков, число сторон дайса]
    b.append(1) if dice[0] == "" else b.append(int(dice[0]))   # если в строке нет числа в начале, присваиваю первому элементу значение 1
    b.append(int(dice[1]))                                     
    return b

# Подсчёт вероятностей
def probs(dice,type = 'p'):
    sums = dict.fromkeys(range(dice[0],dice[0]*dice[1]+1), 0) # создаёт словарь нулей на все возможные суммы
    dice_sides = [i for i in range(1,dice[1]+1)]              # создаёт список из значений на стороных дайса
    denom = dice[1]**dice[0]                                  # знаментаель: количество всех комбинаций

    for i in it.product(dice_sides, repeat=dice[0]):          # модуль комбинаторики перебирает все размещения с повторениями
        s = sum(i)                                            # считаю сумму каждого размещения
        sums[s] += 1                                          # по ключу полученной суммы добавлю единицу
    
    if type == "p":                                           # type = e/p для событий/вероятностей соответственно
        for i in sums:
            sums[i] /= denom
            sums[i] *= 100
    elif type == "e":                                         # если вывод в событиях, sums не меняется
        pass
    else:
        raise Exception("Argument error")                     # если введено что-то кроме e/p, генерируется исключение
    
    return sums