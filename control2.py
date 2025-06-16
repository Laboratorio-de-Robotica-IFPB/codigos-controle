
#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile


# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Create your objects here.
ev3 = EV3Brick()
left_motor = Motor(Port.B, Direction.CLOCKWISE)
right_motor = Motor(Port.C, Direction.CLOCKWISE)
robot = DriveBase(left_motor, right_motor, wheel_diameter=55.5, axle_track=104)

left_sensor = ColorSensor(Port.S2)
right_sensor = ColorSensor(Port.S3)

# Constantes
DRIVE_SPEED = 100
TURN_SPEED = 60

BLACK = 15
WHITE = 80
THRESHOLD = (BLACK + WHITE) / 2

ev3.speaker.beep()
while True:
    #verde>curva 90dg>pid
    robot.drive(DRIVE_SPEED, 0)
    '''wait(30)
    left_reflection = left_sensor.reflection()
    right_reflection = right_sensor.reflection()
    while left_reflection<THRESHOLD:
        if (left_reflection<5):
            robot.stop()
        else:
            robot.drive(TURN_SPEED, -(2000/(left_reflection+12)))
            left_reflection=left_sensor.reflection()
    while right_reflection<THRESHOLD:
        if (right_reflection<5):

        else:
            robot.drive(TURN_SPEED, (2000/(right_reflection+10)))
            right_reflection=right_sensor.reflection()
    #branco=70 a 80
    # preto<20 ou 10
    #verde entre 20 e 60
'''
















    ''' "indeciso"
    # Se um dos sensores vê preto, entra no loop de correção
    if (left_reflection < THRESHOLD or right_reflection < THRESHOLD):
        # Para o robô completamente
        robot.stop()        

        # Se o sensor direito viu preto
        while right_reflection < THRESHOLD and cont<3:
            cont+=1
            # Gira para a direita até o sensor esquerdo detectar preto
            robot.drive(0, TURN_SPEED)
            while left_sensor.reflection() >= THRESHOLD:
                wait(10)
            robot.stop()
            # Dá um pequeno ajuste para alinhar (vira um pouco para a esquerda)
            robot.drive(0, -TURN_SPEED)
            wait(300)
            robot.stop()

        # Se o sensor esquerdo viu preto
        while left_reflection < THRESHOLD and cont<3:
            cont+=1
            # Gira para a esquerda até o sensor direito detectar preto
            robot.drive(0, -TURN_SPEED)
            while right_sensor.reflection() >= THRESHOLD:
                wait(10)
            robot.stop()
            # Dá um pequeno ajuste para alinhar (vira um pouco para a direita)
            robot.drive(0, TURN_SPEED)
            wait(300)
            robot.stop()
    # Continua dirigindo para frente quando os sensores não detectam preto
    else:
        robot.drive(DRIVE_SPEED, 0)
    if cont==3:
        robot.straight(5)
    wait(20)'''
