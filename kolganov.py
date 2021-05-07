"""
Курсовая работа выполнена студентом: Колгановым Владимиром, 20-ЗИЭ
Дисциплина: Программирование
Задание: «Получение сведений о сотрудниках»
Отсортировать список по возрастанию стажа работы сотрудников
Исходный файл: kolganov_sotrudniki.txt
Имя файла программы: kolganov.py

Программа написана по стандарту: PEP 8
"""

lvl_out = []


# Функция формирования списка сотрудников
def file_open(dic):
    with open('sotrudniki.txt', encoding="utf-8") as file:
        for i in file:
            i = i.strip()
            dic = dic + [i]
            dic_chop = [dic[x:4 + x] for x in range(0, len(dic), 4)]
    return dic_chop


# Функция поиска подходящих по условию сотрудников
def search(op_file, lvl_in):
    file_out = []
    for i in range(len(op_file)):
        if int(op_file[i][3]) > lvl_in:
            file_out.append(op_file[i])
    return file_out


# Функция сортировки списков по возрастанию стажа
def sort(lst):
    print(lst)
    new_result = sorted(lst, key=lambda arg: int(arg[3]))
    return new_result


# Функция форматированного вывода результатов на экран
def output(lst):
    a = 0
    b = 0
    c = 0
    if len(lst) == 0:
        print('Нет сотрудников удовлетворяющих введенным требованиям.')
    else:
        print("Кол-во сотрудников удволетворяющих требованию: %s" % len(lst))
        for i in range(len(lst)):
            if len(lst[i][0]) > a:
                a = len(lst[i][0])
            if len(lst[i][1]) > b:
                b = len(lst[i][1])
            if len(str(i+1)) > c:
                c = len(str(i+1))
        for i in range(len(lst)):
            print("%s-й: Фамилия: %s | Отдел: %s | Дата рожденья: %s | Стаж работы: %s." %
                  (str(i+1).rjust(c), lst[i][0].ljust(a), lst[i][1].ljust(b), lst[i][2], lst[i][3]))


# Основная программа
if __name__ == '__main__':
    try:
        # Ввод данных пользователем
        lvl_input = input("Введите стаж работы сотрудника(в месяцах): ")
        # Проверяем на правильность ввода данных
        if lvl_input.isdigit():
            lvl_input = int(lvl_input)
        else:
            # Вызываем Except TypeError
            raise TypeError("Неправильный ввод данных! Вводите только положительные числа!")
    except ZeroDivisionError:
        print("Что-то пошло не так!")
    else:
        # Получаем списки подходящих по условию сотрудников
        result = search(file_open(lvl_out), lvl_input)
        # Вызов функции сортировки и вывода результатов на экран
        output(sort(result))
