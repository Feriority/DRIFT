# Events when near Shiny and Chrome

init 1 python:
    import store.gamestate as gamestate

    class ShinyChromePassiveEvent(classes.Event):
        def isValid(self):
            return (
                gamestate.are_adjacent('shinychrome', 'racer') and
                gamestate.racers['shinychrome'].disposition >= 0
            )

    class ShinyChromeAggroEvent(classes.Event):
        def isValid(self):
            return (
                gamestate.are_adjacent('shinychrome', 'racer') and
                gamestate.racers['shinychrome'].disposition < 0
            )

    ShinyChromePassiveEvent('shiny_and_chrome_passive')
    ShinyChromeAggroEvent('shiny_and_chrome_aggro')

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

    $ success = renpy.random.random()

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

label shiny_and_chrome_aggro:
    $ pos_diff = gamestate.position_diff('shinychrome', 'racer')
    if pos_diff < 0:
        # Shiny and Chrome are ahead
        show racer_sprite at left with moveinleft

        "Shiny and Chrome are out in front of you."
        show v8_interceptor at right with moveinright

        "Suddenly, they whip their Interceptor around and start driving at you head on!"

        show chrome_sprite at right with moveinbottom
    else:
        # Shiny and Chrome are behind
        show racer_sprite at right with moveinright

        "An engine roar fills you ears right before your entire car shakes."
        with hpunch

        # TODO: Do damage to player's car

        "Shiny and Chrome just rammed you!"
        show v8_interceptor at left with moveinleft

        "Looks like they're setting up to do it again!"

        show chrome_sprite at left with moveinbottom

    "Chrome climbs out of the passenger side window holding a spear with a metal capsule at the end."
    gamestate.actors['chrome'] "Witness me!"

    menu:
        "Witness her.":
            "You don't move an inch, transfixed by Chrome and her spear."
            jump shiny_and_chrome_speared
        "Attmept to dodge.":
            "You swerve to avoid the impending danger."
            "Shiny and Chrome anticipated this, however, and they correct their course just in time."
            jump shiny_and_chrome_speared
        "Slam on the brakes.":
            "The tires on your car smoke and screech, and you lurch forward in your seat."
            "Shiny and Chrome falter, not expecting such a move, and drive past your car instead of into it."
            "Chrome stabs the spear at your car. There's an explosion, but you come out unscathed. She must have missed."

            menu:
                "Get away!":
                    "Speeding ahead to avoid a counterattack, you put enough distance between you and the Interceptor to breath easy again."
                    jump shiny_and_chrome_exit_ahead
                "Retaliate!":
                    "You turn your car to ram them back."
                    "Just before impact, Chrome pulls another spear out of the Interceptor and thrusts it at you!"
                    gamestate.actors['chrome'] "FOOL!"
                    with hpunch
                    "Another explosion shakes the road, and this time the spear hit its mark."
                    "You crash into Shiny and Chrome, and both vehicles careen to the track wall."

                    # TODO: Do heavy damage to both cars

                    "After untangling the cars from each other, you both rejoin the race, though your car is worse for wear."
                    $ gamestate.changeStanding('shinychrome', 2)
                    $ gamestate.changeStanding('racer', 2)

                    jump shiny_and_chrome_exit_behind
                "DRIFT!":
                    "You drift around a bend in the road, leaving Shiny and Chrome behind."
                    jump shiny_and_chrome_exit_ahead
        "DRIFT!":
            "You drift into the oncoming attack."
            "Chrome strikes with the spear, but your spoiler hits it mid lunge, snapping it in two!"
            "The spear tip rolls under Shiny and Chrome's Interceptor and detonates."
            with hpunch
            "The explosion rocks Shiny and Chrome, spinning them to the track wall."

            # TODO: Do heavy damage to Shiny and Chrome

            "You drift away, completely unphrased."

            $ gamestate.changeStanding('shinychrome', 2)

            jump shiny_and_chrome_exit_ahead

    # Should never hit this, but just in case
    jump shiny_and_chrome_exit_ahead

label shiny_and_chrome_speared:
    "As your cars collide, Chrome drives the spear into your vehicle."
    with hpunch
    "It explodes!"

    # TODO: Do heavy damage to player's car

    "The impact and explosion sends your racer spinning to the track wall."
    "Shiny and Chrome circle around past you to get a look before speeding down the track."

    $ gamestate.changeStanding('racer', 2)

    jump shiny_and_chrome_exit_behind

label shiny_and_chrome_exit_ahead:
    $ pos_diff = gamestate.position_diff('shinychrome', 'racer')
    if pos_diff < 0:
        $ gamestate.changeStanding('racer', -1)

    hide v8_interceptor
    hide chrome_sprite
    with moveoutleft

    hide racer_sprite with moveoutright

label shiny_and_chrome_exit_behind:
    $ pos_diff = gamestate.position_diff('shinychrome', 'racer')
    if pos_diff > 0:
        $ gamestate.changeStanding('racer', 1)

    hide v8_interceptor
    hide chrome_sprite
    with moveoutright

    hide racer_sprite with moveoutleft
