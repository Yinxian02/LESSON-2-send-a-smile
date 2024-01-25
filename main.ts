input.onButtonPressed(Button.A, function () {
    basic.clearScreen()
    radio.sendString("tealy")
    timer = 0
})
radio.onReceivedString(function (receivedString) {
    basic.showString(receivedString)
    basic.showLeds(`
        . . . . .
        # . . . #
        # . . . #
        # . . . #
        . # # # .
        `)
    timer = 0
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
timer = 0
basic.showLeds(`
    . . . . .
    . . . . .
    # # # # #
    . . . . .
    . . . . .
    `)
radio.setGroup(1)
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
