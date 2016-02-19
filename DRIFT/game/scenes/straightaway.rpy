# straightaway scene
# currently this is only an example for testing purposes

init 1 python:
    classes.StraightawayEvent("straightaway_1")

label straightaway_1:
    show racer_sprite at left with moveinleft

    "The road stretches straight ahead. None of the other drivers are in your way."

    $ racer_standing = gamestate.standings.index(gamestate.racers['racer'])
    menu:
        "Speed ahead to again some ground.":
            "You step on the gas and fly down the track."

            $ next_standing = racer_standing - 1
            if next_standing >= 0:
                $ racer_ahead = gamestate.standings[next_standing]
                "Along the way, you pass by [racer_ahead.characterName]."

            hide racer_sprite with moveoutright

            $ gamestate.changeStanding('racer', -1)
        "Ease up on the gas.":
            "You slow down and relax for a moment."

            $ prev_standing = racer_standing + 1
            $ num_racers = len(gamestate.standings)
            if prev_standing < num_racers:
                $ racer_behind = gamestate.standings[prev_standing]
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
