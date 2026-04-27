def wait_for_button(ev3):
    """
    Esta funcion espera hasta que haya un boton presionado y da el resultado a main.py.
    """
    pressed = []
    while len(pressed) != 1:
        pressed = ev3.buttons.pressed()
    button = pressed[0]

    ev3.screen.draw_text(2, 100, button)

    while any(ev3.buttons.pressed()):
        pass

    return button
