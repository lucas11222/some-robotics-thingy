#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color, Button
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

# Importar la funcion.
from buttons import wait_for_button

# Hablar al EV3
ev3 = EV3Brick()


# Loop
is_running = True
while is_running == True:
    # Esperar al presionar un boton.
    button = wait_for_button(ev3)

    # Si presionas el boton CENTER (centrar) parar el programa
    if button == Button.CENTER:
        ev3.speaker.beep(200)
        ev3.light.on(Color.BLUE)
        wait(200)
        ev3.light.off()
        is_running = False
    if button == Button.LEFT_UP:
        ev3.speaker.set_speech_options("es", None, None, None)
        ev3.speaker.say("hola")
    if button == Button.LEFT_UP:
        ev3.speaker.set_speech_options("es", None, None, None)
        ev3.speaker.say("hola")