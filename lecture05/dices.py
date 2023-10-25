import itertools as it
import re

# проверка корректности ввода
def check(a):
    if re.fullmatch(r'\d{0,2}d\d{1,}',a):                      # проверяет полное совпадение с шаблонной строкой: от нуля до двух цифр, d, не менее одной цифры
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
def probs(dices:list,type = 'p'):

    dice_sides = []
    a = 0
    for dice in dices:
        a += dice[0]*dice[1] 
        b = [i for i in range(1,dice[1]+1)]
        for _ in range(0,dice[0]): dice_sides.append(b)        # создаёт список из значений на стороных дайса
    sums = dict.fromkeys(range(1,a+1), 0)                      # создаёт словарь нулей на все возможные суммы (от единицы - так удобнее)

    denom = 0
    for i in it.product(*dice_sides):                          # модуль комбинаторики перебирает все размещения с повторениями
        s = sum(i)                                             # считаю сумму каждого размещения
        sums[s] += 1                                           # по ключу полученной суммы добавлю единицу
        denom += 1

    if type == "p":                                            # type = e/p для событий/вероятностей соответственно
        for i in sums:
            sums[i] /= denom
            sums[i] *= 100
    elif type == "e":                                          # если вывод в событиях, sums не меняется
        pass
    else:
        raise Exception("Argument error")                      # если введено что-то кроме e/p, генерируется исключение
    
    return dict(filter(lambda x: x[1] != 0 , sums.items()))    # на выход идёт словарь из которого исключены нулевые суммы