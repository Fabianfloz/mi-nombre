basic.forever(function () {
    basic.showLeds(`
        . # # # .
        . # . . .
        . # # . .
        . # . . .
        . # # # .
        `)
    basic.pause(2)
    basic.showLeds(`
        . . . # .
        . . . # .
        . # # # .
        . # . # .
        . # # # .
        `)
    basic.pause(2)
    basic.showLeds(`
        . # . # .
        . # . # .
        . # # # .
        . . # . .
        . . # . .
        `)
    basic.pause(2)
    basic.showLeds(`
        # . . # .
        # # . # .
        # . # # .
        # . . # .
        # . . # .
        `)
})
