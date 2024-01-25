def on_button_pressed_a():
    global timer
    basic.clear_screen()
    radio.send_string("tealy")
    timer = 0
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_received_string(receivedString):
    global timer
    basic.show_string(receivedString)
    basic.show_leds("""
        . . . . .
        # . . . #
        # . . . #
        # . . . #
        . # # # .
        """)
    timer = 0
radio.on_received_string(on_received_string)

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
timer = 0
basic.show_leds("""
    . . . . .
    . . . . .
    # # # # #
    . . . . .
    . . . . .
    """)
radio.set_group(1)

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
