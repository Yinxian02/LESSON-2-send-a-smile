// def on_button_pressed_a():
// basic.clear_screen()
// input.on_button_pressed(Button.A, on_button_pressed_a)
// def on_received_string(receivedString):
// pass
// radio.on_received_string(on_received_string)
input.onButtonPressed(Button.A, function () {
    timer = 0
    basic.showLeds(`
        . . . . .
        # . . . #
        # . . . #
        # . . . #
        . # # # .
        `)
})
input.onButtonPressed(Button.B, function () {
    control.reset()
})
input.onGesture(Gesture.Shake, function () {
    basic.showString("Tealy")
    timer = 0
    basic.showLeds(`
        . # # # .
        # . . . #
        # . . . #
        # . . . #
        . # # # .
        `)
})
let timer = 0
basic.showLeds(`
    . . . . .
    . . . . .
    # # # # #
    . . . . .
    . . . . .
    `)
basic.forever(function () {
    basic.pause(1000)
    timer += 1
    if (timer == 15) {
        basic.showLeds(`
            . . . . .
            . # # # .
            # . . . #
            # . . . #
            # . . . #
            `)
    }
    if (timer == 30) {
        while (true) {
            basic.showLeds(`
                . . . . .
                . # # # .
                # . . . #
                # . . . #
                # # # # #
                `)
        }
    }
})
