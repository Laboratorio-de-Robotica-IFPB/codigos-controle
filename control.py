base = 270
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
speed = 200
turn_rate = 80

ti = time.time()
while(True):
    drive_base.drive(speed, 0)

  #  print(d, c)
    k = (1.0 if d > c else -1.0)
    #k = (-1.0 if c > d else 1.0)
    #if abs(d - c) < 20:
    #    s = 0

    if abs(d - c) < 50:
        k = 0
    #    s = ((d - c) / (d + c)) * (-1)
    #else:
    #    s = 0 


   #ainda vou ver se isso funciona:
    '''r1, g1, b1=left_sensor.rgb()
    r2, g2, b2=right_sensor.rgb()
    if g1>=80 and g2>=80:
        right_motor.run_time(base, 2000)
        left_motor.run_time(base/10, 2000)
    else if g1>=80:
        right_motor.run_time(base, 1000)
        left_motor.run_time(base/10, 1000)
    else if g2>=80:
        left_motor.run_time(base, 1000)
        right_motor.run_time(base/10, 1000)
    '''
       if color_left <= 20:
        while(color_left <= 20):
            right_motor.run(base)
            left_motor.run(base/10)
            rl, gl, bl = left_sensor.rgb()
            color_left = (rl + gl + bl)


 '''
 rl, gl, bl = left_sensor.rgb()
    rr, gr, br = right_sensor.rgb()

    tf = time.time()
    #print("right =  ({}, {}, {})".format(rr,gr,br))
   # print("left =  ({}, {}, {})".format(rl,gl,bl))
    
    color_left = (rl + gl + bl)
    color_right = (rr + gr + br)

    c = control(b, color_left, prevc, ti)
    d = control(b, color_right, prevd, ti)

    k = (1.0 if d > c else -1.0)
    if abs(d - c) < 50:
        k = 0
    if color_left <= 20:
        left_motor.stop()
        while(color_right >= 80):
            rr, gr, br = right_sensor.rgb()
            color_right = (rr + gr + br)
            d = control(b, color_right, prevd, ti)
            right_motor.run(base - d*k)
            left_motor.run(10)
        right_motor.stop()
    if color_right <= 20:
        right_motor.stop()
        while(color_left >= 80):
            rl, gl, bl = left_sensor.rgb()
            color_left = (rl + gl + bl)
            c = control(b, color_left, prevc, ti)
            left_motor.run(base + c*k)
            right_motor.run(10)
        left_motor.stop()
    right_motor.run(base - d*k)
    left_motor.run(base + c*k) 
    
    prevc = color_left
    prevd = color_right
    '''
