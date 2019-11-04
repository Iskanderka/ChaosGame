import turtle  # модуль, позволяющий рисовать на базовом уровне
from random import randint, choice  # для случайных прыжков


def draw_next_mid_dot(in_angles):
    """Отмеряет половину расстояния до случайной вершины,
    перемещается на это расстояние и ставит точку под собой
    принимает количество углов"""
    next_apex_number = randint(0, in_angles-1)  # рандомим номер следующей вершины
    next_apex_x = (apexes[next_apex_number][0] + turtle.xcor()) / 2  # вычисляем координаты середины пути до вершины
    next_apex_y = (apexes[next_apex_number][1] + turtle.ycor()) / 2
    turtle.goto(next_apex_x, next_apex_y)  # перемещаемся на вычисленные координаты
    turtle.dot(4, choice(colors))


def triangle_base():
    """Вырисовывает вершины треугольника и возвращает
    двумерный список с координатами вершин"""
    radius_lol = 2 * (
                (side_length ** 2 - (side_length / 2) ** 2) ** 0.5) / 3  # вычисляем путь до первой вершины из центра

    turtle.right(30)  # добегаем до одной из вершин и ставим там отметку
    turtle.forward(radius_lol)
    turtle.stamp()
    in_apexes = [[turtle.xcor(), turtle.ycor()]]  # запоминаем координаты первой вершины

    turtle.left(150)  # добегаем до другой и ставим там отметку
    turtle.forward(side_length)
    turtle.right(30)
    turtle.stamp()
    in_apexes.append([turtle.xcor(), turtle.ycor()])  # запоминаем координаты второй вершины

    turtle.left(150)  # добегаем до третьей вершины и ставим последнюю точку
    turtle.forward(side_length)
    turtle.right(30)
    turtle.stamp()
    in_apexes.append([turtle.xcor(), turtle.ycor()])  # запоминаем координаты последней вершины

    return in_apexes


# def square_base():  # пока не работает, в будущем, может, это будет вообще одна функция для всевозможных фигур
#     """Вырисовывает вершины квадрата и возвращает
#         двумерный список с координатами вершин"""
#     radius_lol = ((
#                 (side_length / 2) ** 2 + (side_length / 2) ** 2) ** 0.5)  # вычисляем путь до первой вершины из центра
#
#     turtle.right(45)  # добегаем до одной из вершин и ставим там отметку
#     turtle.forward(radius_lol)
#     turtle.stamp()
#     in_apexes = [[turtle.xcor(), turtle.ycor()]]  # запоминаем координаты первой вершины
#
#     turtle.left(135)  # добегаем до другой и ставим там отметку
#     turtle.forward(side_length)
#     turtle.right(45)
#     turtle.stamp()
#     in_apexes.append([turtle.xcor(), turtle.ycor()])  # запоминаем координаты второй вершины
#
#     turtle.left(135)  # добегаем до другой и ставим там отметку
#     turtle.forward(side_length)
#     turtle.right(45)
#     turtle.stamp()
#     in_apexes.append([turtle.xcor(), turtle.ycor()])  # запоминаем координаты второй вершины
#
#     turtle.left(135)  # добегаем до последней вершины и ставим последнюю точку
#     turtle.forward(side_length)
#     turtle.right(45)
#     turtle.stamp()
#     in_apexes.append([turtle.xcor(), turtle.ycor()])  # запоминаем координаты последней вершины
#
#     return in_apexes
#
#
# def five_angle_base():
#     """Вырисовывает вершины пятиугольника и возвращает
#         двумерный список с координатами вершин"""
#     radius_lol = 2 * (
#             (side_length ** 2 - (side_length / 2) ** 2) ** 0.5) / 3  # вычисляем путь до первой вершины из центра
#
#     turtle.right(30)  # добегаем до одной из вершин и ставим там отметку
#     turtle.forward(radius_lol)
#     turtle.stamp()
#     in_apexes = [[turtle.xcor(), turtle.ycor()]]  # запоминаем координаты первой вершины
#
#     turtle.left(150)  # добегаем до другой и ставим там отметку
#     turtle.forward(side_length)
#     turtle.right(30)
#     turtle.stamp()
#     in_apexes.append([turtle.xcor(), turtle.ycor()])  # запоминаем координаты второй вершины
#
#     turtle.left(150)  # добегаем до третьей вершины и ставим последнюю точку
#     turtle.forward(side_length)
#     turtle.right(30)
#     turtle.stamp()
#     in_apexes.append([turtle.xcor(), turtle.ycor()])  # запоминаем координаты последней вершины
#
#     return in_apexes
#
#
# def six_angle_base():
#     """Вырисовывает вершины шестиугольника и возвращает
#         двумерный список с координатами вершин"""
#     radius_lol = 2 * (
#             (side_length ** 2 - (side_length / 2) ** 2) ** 0.5) / 3  # вычисляем путь до первой вершины из центра
#
#     turtle.right(30)  # добегаем до одной из вершин и ставим там отметку
#     turtle.forward(radius_lol)
#     turtle.stamp()
#     in_apexes = [[turtle.xcor(), turtle.ycor()]]  # запоминаем координаты первой вершины
#
#     turtle.left(150)  # добегаем до другой и ставим там отметку
#     turtle.forward(side_length)
#     turtle.right(30)
#     turtle.stamp()
#     in_apexes.append([turtle.xcor(), turtle.ycor()])  # запоминаем координаты второй вершины
#
#     turtle.left(150)  # добегаем до третьей вершины и ставим последнюю точку
#     turtle.forward(side_length)
#     turtle.right(30)
#     turtle.stamp()
#     in_apexes.append([turtle.xcor(), turtle.ycor()])  # запоминаем координаты последней вершины
#
#     return in_apexes


colors = ['aqua', 'blue', 'fuchsia', 'green', 'maroon', 'orange',  # задаём базу цветов
          'pink', 'purple', 'red', 'yellow', 'violet', 'indigo', 'chartreuse', 'lime']

side_length = 500

turtle.bgcolor("black")  # делаем красоту
turtle.pencolor("white")
turtle.shape("turtle")

turtle.penup()  # прячем чюрюпаху и отбираем у неё карандаш
turtle.hideturtle()

choise = int(turtle.textinput("Выбор фигуры", "Кол-во углов в фигуре, которая будет заполняться: 3, 4, 5, 6"))
# будет иметь значение после того, как я придумаю что делать с фигурами кроме треугольника

# if choise == 3:  # свич с вводом от пользователя с дефолтом в треугольник
#     apexes = triangle_base()
#     angles = 3
# elif choise == 4:
#     apexes = square_base()
#     angles = 4
# elif choise == 5:
#     side_length = 400
#     apexes = five_angle_base()
#     angles = 5
# elif choise == 6:
#     side_length = 300
#     apexes = six_angle_base()
#     angles = 6
# else:
#     apexes = triangle_base()
#     angles = 3

apexes = triangle_base()
angles = 3

for i in range(2000):  # запускаем отрисовку точек
    draw_next_mid_dot(angles)  # в будущем хотелось бы передавать этой функции только количество итераций

turtle.done()  # это чтобы окно после отрисовки не закрывалось
