def on_button_pressed_a():
    global timer
    timer = 0
    basic.clear_screen()
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_received_string(receivedString):
    pass
radio.on_received_string(on_received_string)

def on_button_pressed_a():
    global timer
    timer = 0
    basic.show_leds("""
        . . . . .
        # . . . #
        # . . . #
        # . . . #
        . # # # .
        """)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    control.reset()
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_gesture_shake():
    global timer
    basic.show_string("Tealy")
    timer = 0
    basic.show_leds("""
        . # # # .
        # . . . #
        # . . . #
        # . . . #
        . # # # .
        """)
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

timer = 0
basic.show_leds("""
    . . . . .
    . . . . .
    # # # # #
    . . . . .
    . . . . .
    """)

def on_forever():
    global timer
    basic.pause(1000)
    timer += 1
    if timer == 15:
        basic.show_leds("""
            . . . . .
            . # # # .
            # . . . #
            # . . . #
            # . . . #
            """)
    if timer == 30:
        while True:
            basic.show_leds("""
                . . . . .
                . # # # .
                # . . . #
                # . . . #
                # # # # #
                """)
basic.forever(on_forever)
