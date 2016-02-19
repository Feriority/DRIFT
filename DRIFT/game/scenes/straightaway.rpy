# straightaway scene
# currently this is only an example for testing purposes

init 1 python:
    classes.StraightawayEvent("straightaway_1")

label straightaway_1:
    show racer_sprite at left with moveinleft

    "The road stretches straight ahead. None of the other drivers are in your way."

    $ racer_standing = gamestate.racers['racer'].getPosition()
    menu:
        "Speed ahead to again some ground.":
            "You step on the gas and fly down the track."

            $ racer_ahead = gamestate.getRacerAt(racer_standing - 1)
            if racer_ahead is not None:
                "Along the way, you pass by [racer_ahead.characterName]."

            hide racer_sprite with moveoutright

            $ gamestate.changeStanding('racer', -1)
        "Ease up on the gas.":
            "You slow down and relax for a moment."

            $ racer_behind = gamestate.getRacerAt(racer_standing + 1)
            if racer_behind is not None:
                "[racer_behind.characterName] takes advantage of the moment to pull ahead of you."

            hide racer_sprite with moveoutleft

            $ gamestate.changeStanding('racer', 1)
        "DRIFT!":
            "You drift... straight into the track wall."
            "It's a straightaway. What did you expect?"

            # TODO: Do damage to player's car

            hide racer with dissolve

            $ gamestate.changeStanding('racer', 2)
    return
