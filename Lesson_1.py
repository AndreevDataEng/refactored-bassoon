a = "Енот"
b = 15
print(a, b)
name = input("Введите ваше имя ")
age = input("Введите ваш возраст ")
surname = input("Введите вашу фамилию ")
eye = input("Введите цвет глаз ")
print("Вас зовут " + name + ' ' + surname + ", вам " + age + " лет, и цвет ваших глаз - " + eye )


time = int(input("Введите время в секундах "))
hours = time // 3600
minutes = (time - hours * 3600) // 60
seconds = time - (hours * 3600 + minutes * 60)
print(f"Время в формате чч:мм:сс   {hours} : {minutes} : {seconds}")


n = int(input("Введите число n - "))
x = (n + int(str(n) + str(n)) + int(str(n) + str(n)+ str(n)))
print("Сумма чисел n + nn + nnn - %d" % x)


n = abs(int(input("Введите целое положительное число ")))
max = n % 10
while n >= 1:
    n = n // 10
    if n % 10 > max:
        max = n % 10
    if n > 9:
        continue
    else:
        print("Максимальная цифра в числе ", max)
        break


profit = float(input("Введите выручку фирмы "))
costs = float(input("Введите издержки фирмы "))
if profit > costs:
    print(f"Фирма получает прибыль. Рентабельность составила {profit / costs:.2f}")
    employers = int(input("Введите количество сотрудников "))
    print(f"Прибыль на одного сторудника сотавила {profit / employers:.2f}")
elif profit == costs:
    print("Фирма работает в ноль")
else:
    print("Фирма работает в убыток")


a = int(input("Введите в км сколько спортсмен пробежал в первый день "))
b = int(input("Ввведите желаемый результат пробежки в км "))
days = 1
km = a
while km < b:
        a = a + 0.1 * a
        days += 1
        km = km + a
print(f"Вы достигнете требуемых показателей на %.d день, не менее %.d км" % (days, b)