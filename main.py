#!/usr/bin/env pybricks-micropython

''' 
SCREAMING BUG
The bug will "chase" an object a certain amount of times and then spin around. 
'''

from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase

# Name a motor
motor = Motor(Port.A)

# Name a motor 
motor2 = Motor(Port.B) 

# Name a motor
motor3 = Motor(Port.C)

# Name a motor
motor4 = Motor(Port.D)

# Name a sensor
sensor2 = TouchSensor(Port.S2)

# Name a sensor
sensor3 = TouchSensor(Port.S3)

# Name the ultrasonic sensor
sensor = UltrasonicSensor(Port.S4)

# Create a name for connecting two motors so that we can call it one
robot = DriveBase(motor, motor2, 56, 114)

# Have the robot "chase" an object a certain amount of times
i = 20

# Have the robot spin in a circle 5 times after it has done it's rotation a certain number of times. 
j = 10

# Have the robot run the program a certain number of times so that we don't have to keep restarting it 
o = 20

# Have the robot continue the loop 20 times
while o > 0:
    # Have the robot "chase" an object a certain amount of times
    i = 20

    # Have the robot spin in a circle 5 times after it has done it's rotation a certain number of times. 
    j = 10

    # Say that if someone touches the touch sensors, it will activate
    while not sensor2.pressed() and not sensor3.pressed():
        wait(10)
    
    # Have the robot beep
    brick.sound.beep()
    
    # Have the robot emit A high pitch(1500 Hz) for one second (1000 ms) at 50% volume 
    brick.sound.beep(1500, 1000, 25)

    # Make the light on the robot red
    brick.light(Color.RED)
    wait(1000)

    # Clear the display
    brick.display.clear()

    # Print ' 'Run.' ' near the middle of the screen 
    brick.display.text("Run.", (60, 50))

    # Print ' 'You Better Run' ' a little bit underneath it 
    brick.display.text("You Better Run", (60, 70))

    # Have the robot continue the loop for a certain number of times.
    while i > 0:
        # Spin Wings at full speed for 2 seconds
        motor3.run(400)
        # Have the robot drive at full speed until it senses something, and then stop right before it
        while sensor.distance() > 150:
            wait(10)
            robot.drive(400, 0)
        robot.stop(stop_type = Stop.BRAKE)
        # Have the robot play a laughing sound when it runs into something
        brick.sound.file(SoundFile.LAUGHING_1, 100)
        robot.drive_time(-200, 0, 1000)
        # Have the back wheel lift up
        motor4.run_time(100, 500)
        # Have the robot rotate
        robot.drive_time(0, 360, 1000)
        # Put the back wheel back on the ground
        motor4.run_time(-100, 500)

        #Have the robot stop going through that loop a certain number of times
        i = i-1

    #Lift up the back wheel
    motor4.run_time(100, 500)
    # Make wings spin at full speed
    motor3.run(400)

    # Have the robot spin in a circle a certain number of times
    while j > 0:
        robot.drive_time(0, 360, 1000)
        # Stop the robot from spinning
        j = j-1
    
    # Put the back wheel back on the ground
    motor4.run_time(-100, 500)

    o = o-1


