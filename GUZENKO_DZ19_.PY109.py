# TASK 1
num1 = int(input('Введите 1 число: '))
num2 = int(input('Введите 2 число: '))
try:
    num3 = num1 / num2
except ZeroDivisionError:
    print('Деление на ноль')
else:
    print(num3 ** 2)
finally:
    print('ГОТОВО')

# TASK 2

try:
    num1_ = int(input('Введите 1 число: '))
    num2_ = int(input('Введите 2 число: '))
    num3_ = num1_ / num2_
except ValueError:
    print('Ошибка преобразования')
except ZeroDivisionError:
    print('Деление на ноль')
except BaseException:
    print('Базовое исключение')
else:
    print(num3_)


# HOMEWORK

def homework():
    str1 = input('Введите 1 число: ')
    str2 = input('Введите 2 число: ')
    try:
        str3 = float(str1) / float(str2)
        return str3
    except ZeroDivisionError:
        print('На ноль делить нельзя!')
        str1 = input('Введите 1 строку: ')
        str2 = input('Введите 2 строку: ')
        str3 = float(str1) / float(str2)
        return str3
    except ValueError:
        print('Введите числа!')
        str1 = input('Введите 1 строку: ')
        str2 = input('Введите 2 строку: ')
        str3 = float(str1) / float(str2)
        return str3


homework()
