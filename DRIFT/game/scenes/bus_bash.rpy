# Event when near the bus
init 1 python:
    import store.gamestate as gamestate

    class BusBashEvent(classes.Event):
        def isValid(self):
            return gamestate.are_adjacent('driver', 'racer') and gamestate.track[gamestate.trackIndex] == 'straightaway'

    BusBashEvent('bus_bash_start')

    driver = gamestate.actors['driver']


label bus_bash_start:
    show racer_sprite at right with moveinright
    $ pos_diff = gamestate.position_diff('driver', 'racer')
    "You're on a long stretch of straight road - nothing to do but go fast."
    if pos_diff < 0:
        "You pull up on the schoolbus."
    else:
        "You can see the bus approaching quickly from behind.  Are those rockets?  Isn't that cheating?  It sails past you before the rockets cut out."
        $ gamestate.changeStanding('racer', 1)
    show bus at left with moveinright
    jump bus_bash_loop

label bus_bash_loop:
    "The bus is in front of you, blocking your path."
    menu:
        "Pass the bus.":
            "You try to pass the bus, but the road is narrow and the bus is bulky.  The driver has no problem cutting you off just by swerving back and forth while cackling madly."
            jump bus_bash_loop
        "PIT maneuver the bus!":
            "I don't know why you thought this would work.  That's a schoolbus."
            "You can hear the screams of small children as the front of your car hits the rear tire of the bus, then goes under it."
            "The last thing you hear is the laughter of the driver over the radio."
            hide racer_sprite with vpunch
            hide bus with moveoutleft
            $ gamestate.changeStanding('racer', 2)
            return
        "Drive backwards.":
            "You decide to show off for the children, and defly spin the car around while switching to reverse.  You drive backwards behind the bus, and rev up hard."
            "The burst of flame from your tailpipe catches the rockets on the back of the bus!  Fortunately, the roar of the explosion drowns out the screams of the passengers."
            hide bus with vpunch
            hide racer with moveoutright
            $ gamestate.changeStanding('driver', 2)
        "DRIFT!":
            "You drift!  But it's a straightaway, so that's not doing you much good.  The bus pulls further ahead; maybe you'll have better luck later."

    hide racer_sprite with moveoutright
    hide bus with moveoutleft
