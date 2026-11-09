import turtle

t = turtle.Turtle()
t.speed(0)
t.pensize(2)

turn = 1
num_turns = 8
state = "INIT"

while state != "STOP":

    if state == "INIT":                      # Начальное -> Движение вверх
        state = "UP"
        t.setheading(90)

    elif state == "UP":                      # Движение вверх
        if turn > num_turns:                 # Циклы завершены -> Остановка
            state = "STOP"
        else:
            t.forward(10)
            x, y = t.position()
            if y >= turn * 10:               # Движение вверх завершено
                state = "LEFT"
                t.setheading(180)

    elif state == "LEFT":                    # Движение влево
        t.forward(10)
        x, y = t.position()
        if x <= -turn * 10:                  # Движение влево завершено
            state = "DOWN"
            t.setheading(270)

    elif state == "DOWN":                    # Движение вниз
        t.forward(10)
        x, y = t.position()
        if y <= -turn * 10:                  # Движение вниз завершено
            state = "RIGHT"
            t.setheading(0)

    elif state == "RIGHT":                   # Движение вправо
        t.forward(10)
        x, y = t.position()
        if x >= turn * 10:                   # Движение вправо завершено
            state = "UP"
            turn = turn + 1                  # Начало нового витка
            t.setheading(90)

turtle.done()
