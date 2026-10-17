//  EMISSOR - Controle remoto
radio.setGroup(1)
basic.showString("T")
//  Feedback visual inicial
//  Frente - Botão A
input.onButtonPressed(Button.A, function on_button_pressed_a() {
    radio.sendString("F")
    basic.showArrow(ArrowNames.North)
})
//  Ré - Botão B
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    radio.sendString("B")
    basic.showArrow(ArrowNames.South)
})
//  Parar - A + B
input.onButtonPressed(Button.AB, function on_button_pressed_ab() {
    radio.sendString("S")
    basic.showIcon(IconNames.No)
})
//  Esquerda - Inclinar esquerda
input.onGesture(Gesture.TiltLeft, function on_gesture_tilt_left() {
    radio.sendString("L")
    basic.showArrow(ArrowNames.West)
})
//  Direita - Inclinar direita
input.onGesture(Gesture.TiltRight, function on_gesture_tilt_right() {
    radio.sendString("R")
    basic.showArrow(ArrowNames.East)
})
