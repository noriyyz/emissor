# EMISSOR - Controle remoto
radio.set_group(1)
basic.show_string("T") # Feedback visual inicial

# Frente - Botão A
def on_button_pressed_a():
    radio.send_string("F")
    basic.show_arrow(ArrowNames.NORTH)
input.on_button_pressed(Button.A, on_button_pressed_a)

# Ré - Botão B
def on_button_pressed_b():
    radio.send_string("B")
    basic.show_arrow(ArrowNames.SOUTH)
input.on_button_pressed(Button.B, on_button_pressed_b)

# Parar - A + B
def on_button_pressed_ab():
    radio.send_string("S")
    basic.show_icon(IconNames.NO)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

# Esquerda - Inclinar esquerda
def on_gesture_tilt_left():
    radio.send_string("L")
    basic.show_arrow(ArrowNames.WEST)
input.on_gesture(Gesture.TILT_LEFT, on_gesture_tilt_left)

# Direita - Inclinar direita
def on_gesture_tilt_right():
    radio.send_string("R")
    basic.show_arrow(ArrowNames.EAST)
input.on_gesture(Gesture.TILT_RIGHT, on_gesture_tilt_right)