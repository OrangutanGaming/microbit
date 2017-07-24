import microbit

updatePeriod = 400

ballY = 2
ballX = 1
paddleY = 2
ballXVelocity = 1
ballYVelocity = 1
gameRunning = False
score = 0

microbit.display.set_pixel(ballX, ballY, 9)
microbit.display.set_pixel(0, paddleY, 9)

def paddleNotUp():
    return paddleY > 0

def paddleNotDown():
    return paddleY < 4

def ballOutOfRange():
    return ballX <= 0

def gameOver():
    global gameRunning
    gameRunning = False
    microbit.display.clear()
    microbit.display.scroll("GAME OVER! SCORE:{}".format(score), 150)

def updateXVelocity():
    if ballX == 4:
        global ballXVelocity
        ballXVelocity = (-1) * ballXVelocity
    elif ballX == 1 and ballY == paddleY:
        global ballXVelocity, score
        ballXVelocity = (-1) * ballXVelocity
        score += 1

def updateYVelocity():
    if ballY == 4 or ballY == 0:
        global ballYVelocity
        ballYVelocity = (-1) * ballYVelocity

def moveBall():
    global ballX, ballY
    microbit.display.set_pixel(ballX, ballY, 0)
    ballX = ballX + ballXVelocity
    ballY = ballY + ballYVelocity
    microbit.display.set_pixel(ballX, ballY, 9)

while True:
    if microbit.button_a.was_pressed():
        if not gameRunning:
            gameRunning = True
            last_update_time = 400
        if paddleNotUp():
            microbit.display.set_pixel(0, paddleY, 0)
            paddleY = paddleY - 1
            microbit.display.set_pixel(0, paddleY, 9)

    elif microbit.button_b.was_pressed():
        if not gameRunning:
            gameRunning = True
            last_update_time = 400
        if paddleNotDown():
            microbit.display.set_pixel(0, paddleY, 0)
            paddleY = paddleY + 1
            microbit.display.set_pixel(0, paddleY, 9)

    if gameRunning:
        if ballOutOfRange():
            gameOver()
        elif microbit.running_time() - last_update_time > updatePeriod:
            last_update_time = microbit.running_time()  # "reset" the timer
            updateXVelocity()
            updateYVelocity()
            moveBall()