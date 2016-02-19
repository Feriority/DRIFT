# Events when near Shiny and Chrome

init 1 python:
    import store.gamestate as gamestate

    class ShinyChromePassiveEvent(classes.Event):
        def isValid(self):
            return (
                gamestate.are_adjacent('shinychrome', 'racer') and
                gamestate.racers['shinychrome'].disposition >= 0
            )

    class ShinyChromeAggressiveEvent(classes.Event):
        def isValid(self):
            return (
                gamestate.are_adjacent('shinychrome', 'racer') and
                gamestate.racers['shinychrome'].disposition < 0
            )

    ShinyChromePassiveEvent('shiny_and_chrome_passive')

label shiny_and_chrome_passive:
    $ pos_diff = gamestate.position_diff('shinychrome', 'racer')
    if pos_diff < 0:
        # Shiny and Chrome are ahead
        show racer_sprite at left with moveinleft

        "You approach Shiny and Chrome from behind and pull up alongside them."
        show v8_interceptor at right with moveinright
    else:
        # Shiny and Chrome are behind
        show racer_sprite at right with moveinright

        "You notice Shiny and Chrome drawing closer in your rear view mirror."
        show v8_interceptor at left with moveinleft

        "They pull up beside you, but don't seem to pay you any notice."

    python:
        success = renpy.random.random()

    menu:
        "Cut them off and get in their way.":
            $ gamestate.racers['shinychrome'].changeDisposition(-5)

            "You nimbly manuever around and ahead of them, and successfully throw off Shiny's driving."
            "When he straightens the Interceptor out, however, the road rumbles with fury as their V8 engine roars."
            jump shiny_and_chrome_exit_ahead
        "Speed up and keep your distance.":
            "You floor it, but so do they. For a while both cars are dead even."

            if success >= 0.25:
                "Eventually, you pull ahead, and Shiny and Chrome back off... for now."

                $ gamestate.racers['shinychrome'].changeDisposition(-1)
                jump shiny_and_chrome_exit_ahead
            else:
                "Try as you might, you can't out accelerate Shiny and Chrome, and they take the lead."
                jump shiny_and_chrome_exit_behind
        "Slow down to get out of their way.":
            "Pulling back from the Interceptor gives Shiny and Chrome all the advantage they need, and they waste no time accelerating past you."
            jump shiny_and_chrome_exit_behind
        "DRIFT!":
            if success >= 0.5:
                "Sliding around and ahead of Shiny and Chrome, it's clear that you nailed the drift."
                "Shiny steers into a drift of his own, but stays in your draft for now."

                $ gamestate.racers['shinychrome'].changeDisposition(1)
            else:
                "You drift... right into their Interceptor!"
                "You crash into them, and they swerve right back at you, but the motion of your drift moves you out of harm's way."
                "When Shiny straightens the Interceptor out, however, the road rumbles with fury as their V8 engine roars."
                # TODO: Do damage to Shiny and Chrome

                $ gamestate.racers['shinychrome'].changeDisposition(-5)

            jump shiny_and_chrome_exit_ahead

    # Should never hit this, but just in case
    jump shiny_and_chrome_exit_ahead

label shiny_and_chrome_exit_ahead:
    $ pos_diff = gamestate.position_diff('shinychrome', 'racer')
    if pos_diff < 0:
        $ gamestate.changeStanding('racer', -1)

    hide v8_interceptor with moveoutleft
    hide racer_sprite with moveoutright

label shiny_and_chrome_exit_behind:
    $ pos_diff = gamestate.position_diff('shinychrome', 'racer')
    if pos_diff > 0:
        $ gamestate.changeStanding('racer', 1)

    hide v8_interceptor with moveoutright
    hide racer_sprite with moveoutleft
