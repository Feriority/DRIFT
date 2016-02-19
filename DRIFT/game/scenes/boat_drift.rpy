# Possible event where a straightaway allows a shortcut

init 1 python:
    class BoatDriftEvent(classes.TurnEvent):
        play_once_only = True

    BoatDriftEvent("boat_drift")

label boat_drift:
    show racer_sprite at left with moveinleft

    "The road follows the curve of a small lake along the course.  Ahead, you can see a slope down to the water, where a short dock with a raft extends into the lake."
    python:
        #TODO: use damage to influence success chance?
        success = renpy.random.random()

    menu:
        "Drive fast.":
            if success >= 0.70:
                $ racer_standing = gamestate.racers['racer'].getPosition()
                $ next_standing = racer_standing - 1
                if next_standing >= 0:
                    $ racer_ahead = gamestate.standings[next_standing]
                    "Your aggressive driving lets you pull ahead of [racer_ahead.characterName], who took the turns more carefully."
                $ gamestate.changeStanding('racer', -1)
            elif success >= 0.20:
                "You keep up your pace.  With the gentle curves of the road, you keep control just fine, although you don't gain much ground."
            else:
                "You pick up speed, but the curves of the road are sharper than you expected.  You lose control, sliding down into the water."
                $ gamestate.changeStanding('racer', 1)
        "Take the curves slower.":
            if success >= 0.50:
                "You slow down, safely handling the twists and turns until clear of the lake."
            else:
                "You slow down, safely handling the road and appreciating your view of the lake."
                $ prev_standing = racer_standing + 1
                $ num_racers = len(gamestate.racers)
                if prev_standing < num_racers:
                    $ racer_behind = gamestate.standings[prev_standing]
                    "[racer_behind.characterName], driving much more aggressively, pulls ahead of you."
                    if success >= 0.20:
                        "They can't keep control during a sharp curve, however, and slide offroad into the water with a splash."
                        $ gamestate.changeStanding(racer_behind.key, 1)
                    else:
                        $ gamestate.changeStanding('racer', 1)
        "DRIFT!":
            "You drift through a corner... down the slope, across the dock, and onto the raft.  You hit it sideways, and your momentum pushes it out into the water."
            menu:
                "Hit the gas.":
                    "You accelerate... straight off the raft and into the water.  How did you think that was going to go?"
                    $ gamestate.changeStanding('racer', 2)
                "Reverse.":
                    "You switch to reverse and back up... straight off the raft and into the water.  How did you think that was going to go?"
                    $ gamestate.changeStanding('racer', 2)
                "DRIFT!":
                    "You hit the brakes and the raft drifts across the lake, with you aboard.  You hit it pretty fast, and cutting through the lake saves you from the long route along its shore - you think you actually gained some time."
                    show racer_sprite at right with moveinleft
                    $ gamestate.changeStanding('racer', -1)
    hide racer_sprite with moveoutright
