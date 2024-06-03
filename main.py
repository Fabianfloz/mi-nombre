def on_forever():
    basic.show_leds("""
        . # # # .
        . # . . .
        . # # . .
        . # . . .
        . # # # .
        """)
    basic.pause(2)
    basic.show_leds("""
        . . . # .
        . . . # .
        . # # # .
        . # . # .
        . # # # .
        """)
    basic.pause(2)
    basic.show_leds("""
        . # . # .
        . # . # .
        . # # # .
        . . # . .
        . . # . .
        """)
    basic.pause(2)
    basic.show_leds("""
        # . . # .
        # # . # .
        # . # # .
        # . . # .
        # . . # .
        """)
basic.forever(on_forever)
