def solution(a, b, c):
    if (a == 0) or (b == 0) or (c == 0):
        print("Ошибка")
    else:
        D = b ** 2 - 4 * a * c
        if D < 0:
            print("Нет корней")
        elif D == 0:
            print("Корень уравнения: ", (-b) / (2 * a))
        else:
            x1 = (-b + D ** (0.5)) / (2 * a)
            x2 = (-b - D ** (0.5)) / (2 * a)
            print("Корни уравнения: x1 =", x1, " x2= ", x2)


a = int(input("Введите коэффицент a>>"))
b = int(input("Введите коэффицент b>>"))
c = int(input("Введите коэффицент c>>"))
solution(a, b, c)
