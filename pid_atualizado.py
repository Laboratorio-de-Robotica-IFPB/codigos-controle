#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor
from pybricks.parameters import Port

# Create your objects here

# Initialize the EV3 Brick.
ev3 = EV3Brick()
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor, InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
# Initialize a motor at port B.
left_motor = Motor(Port.B, Direction.CLOCKWISE)
right_motor = Motor(Port.C, Direction.CLOCKWISE)
robot = DriveBase(left_motor, right_motor, wheel_diameter=55.5, axle_track=104)
# Play a sound.
ev3.speaker.beep()
left_sensor=ColorSensor(Port.S2)
right_sensor=ColorSensor(Port.S3)
# Run the motor up to 500 degrees per second. To a target angle of 90 degrees.
# Play another beep sound.
base = 100
Ki = 1.7
Kd = 3
b = 280
prevc = 0
prevd = 0

time = StopWatch()

def control(setpoint, x, prev, ti):
    erro = setpoint - x
    P = Ki * erro
    derivada = (erro - prev) / (time.time() - ti)
    D = derivada * Kd
    return P + D

turn_rate = 80

ti = time.time()
right_motor.run(base)
left_motor.run(base)
while(True):
    #-----Sensores-------
    rl, gl, bl = left_sensor.rgb()
    rr, gr, br = right_sensor.rgb()
    color_left = (rl + gl + bl)
    color_right = (rr + gr + br)

    '''#------teste-----
    print("verde",gl, gr, "vermelho", rl, rr, "azul", bl, br)
    wait(200)
    #branco: verde 70-95, vermelho 70-75, azul 100
    #verde: verde >=45. vermelho e azul <=41
    '''
    
    #---controle-------
    c = control(b, color_left, prevc, ti)
    d = control(b, color_right, prevd, ti)
    tf = time.time()
    
    #print("right =  ({}, {}, {})".format(rr,gr,br))
    #print("left =  ({}, {}, {})".format(rl,gl,bl))
    
    k = (1.0 if d > c else -1.0)
    #k = (-1.0 if c > d else 1.0)
    
    #if abs(d - c) < 20:
    #    s = 0

    if abs(d - c) < 50:
        k = 0
        s = ((d - c) / (d + c)) * (-1)
    else:
        s = 0

    '''#------verde----------
    if 2*gl>=bl+rl and 2*gr>=br+rr:
        right_motor.run_time(base, 2000)
        left_motor.run_time(base/10, 2000)
    elif 2*gl>=bl+rl:
        right_motor.run_time(base, 1000)
        left_motor.run_time(base/10, 1000)
    elif 2*gr>=br+rr:
        left_motor.run_time(base, 1000)
        right_motor.run_time(base/10, 1000)
'''
    #----controle pid (segue linha)--------
    while color_left<=20 and color_right<=20:
        #continuar andando
        right_motor.run(base)
        left_motor.run(base)
        rl, gl, bl = left_sensor.rgb()
        rr, gr, br = right_sensor.rgb()
        color_left = (rl + gl + bl)
        color_right = (rr + gr + br)
    if color_left <= 20:
        left_motor.stop()
        #while(color_right >= 80):
        while color_left<=90:
            #rr, gr, br = right_sensor.rgb()
            #color_right = (rr + gr + br)
            rl, gl, bl=left_sensor.rgb()
            color_left=rl+gl+bl
            d = control(b, color_right, prevd, ti)
            right_motor.run(base - d*k)
            left_motor.run(20)
            #left_motor.run(10)
            wait(40) 
        right_motor.stop()
    if color_right <= 20:
        right_motor.stop()
        #while(color_left >= 80):
        while color_right<=90:
            #rl, gl, bl = left_sensor.rgb()
            #color_left = (rl + gl + bl)
            rr, gr, br = right_sensor.rgb()
            color_right = (rr + gr + br)
            c = control(b, color_left, prevc, ti)
            left_motor.run(base + c*k)
            #right_motor.run(10)
            right_motor.run(20)
            wait(40)
        left_motor.stop()
    right_motor.run(base -  d*k)
    left_motor.run(base + c*k) 
    prevc = color_left
    prevd = color_right
