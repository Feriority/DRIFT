# turn scene
# currently this is only an example for testing purposes

init 1 python:
    classes.TurnEvent("turn_1")

label turn_1:
    show racer_sprite at left with moveinleft

    "Up ahead, the road bends as it passes through a small gorge with steep, rocky walls."

    python:
        racer_standing = gamestate.racers['racer'].getPosition()

        success = renpy.random.random()

    menu:
        "Take the inside.":
            $ racer_ahead = gamestate.getRacerAt(racer_standing - 1)
            if racer_ahead is None:
                #TODO: use racer damage to influence success chance?
                if success >= 0.60:
                    "You cut the corner perfectly, and fly out the other side of the gorge at top speed."
                else:
                    "You steer across the track, but a wheel slips and the car lurches a little too far."
                    "There's a loud scraping sound as car meets wall, but you correct your motion before too much damage is done."
                    # TODO: Do slight damage to player's car

                jump turn_exit_ahead
            else:
                # TODO use racer and racer_ahead's damage to influence success
                if success >= 0.50:
                    "The jerk in [racer_ahead.characterName]'s driving gives away their surprise as you cut inside them to pull ahead."
                    # TODO: Decrease racer_ahead's disposition?
                    $ gamestate.changeStanding('racer', -1)

                    jump turn_exit_ahead
                else:
                    "You've almost pulled ahead of [racer_ahead.characterName], but they cut you off at the last minute."
                    if success < 0.20:
                        "Getting out of their way proves difficult, however, and you slam into the wall before regaining control."
                        # TODO: Do damage to player's car

                    jump turn_exit_behind
        "Play it safe.":
            "You stay to the outside of the track to avoid crashing."

            $ racer_behind = gamestate.getRacerAt(racer_standing + 1)
            if racer_behind is not None:
                "However, [racer_behind.characterName] tries to take advantage of this and slip past you on the inside."

                menu:
                    "Cut them off.":
                        # TODO: Decrease racer_behind's disposition
                        # TODO: user racer and racer_behind's damage to influence success
                        if success >= 0.50:
                            "You turn to get in their way and block their advance."
                            if success >= 0.80:
                                "[racer_behind.characterName] swerves out of the way... and into the wall."
                                "There's only the sound of metal crunching against rock as you disappear around the corner."
                                # TODO: Do damage to racer_behind's car
                            else:
                                "[racer_behind.characterName] slams on the breaks so hard that you can feel their rage."
                                "Not your problem now, though."

                            jump turn_exit_ahead
                        else:
                            "You turn to get in their way, but it's too late! [racer_behind.characterName] has the edge and pushes you aside."
                            $ gamestate.changeStanding('racer', 1)

                            jump turn_exit_behind
                    "Let them go.":
                        "While holding your course, [racer_behind.characterName] drives right by."
                        # TODO: Increase racer_behind's disposition
                        $ gamestate.changePosition('racer', 1)

                        jump turn_exit_behind
                    "DRIFT!":
                        "You drift gracefully through the rest of the turn, while [racer_behind.characterName] backs off."
                        # TODO: Increase racer_behind's disposition

                        jump turn_exit_ahead
        "DRIFT!":
            "You oversteer to start the drift as you enter the gorge."
            "It's tight, but your car begins to slide and turn just in time."
            "Your back corner scrapes against the wall, throwing up a cloud of dust."

            $ racer_1_behind = gamestate.getRacerAt(racer_standing + 1)
            $ racer_2_behind = gamestate.getRacerAt(racer_standing + 2)
            if racer_1_behind is not None and racer_2_behind is not None:
                "The dust forces [racer_1_behind.characterName] to slow down, allowing [racer_2_behind.characterName] to pass them."
                $ gamestate.changeStanding(racer_1_behind, 1)

            jump turn_exit_ahead

    # Should never hit this, but just in case
    jump turn_exit_ahead

label turn_exit_ahead:
    hide racer_sprite with moveoutright

label turn_exit_behind:
    hide racer_sprite with moveoutleft
