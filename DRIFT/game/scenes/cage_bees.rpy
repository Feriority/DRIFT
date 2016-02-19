# event when near Nic Cage

init 1 python:
    import store.gamestate as gamestate

    class CageBeesEvent(classes.Event):
        def isValid(self):
            return gamestate.are_adjacent('cage', 'racer')

    CageBeesEvent("cage_bees")

    cage = gamestate.actors['cage']

label cage_bees:
    $ pos_diff = gamestate.position_diff('cage', 'racer')
    if pos_diff < 0:
        # Nic Cage is ahead
        show racer_sprite at left with moveinleft

        "Nicolas Cage is ahead of you."
        show cage_sprite at right
        show bike at right
        with moveinright

        menu:
            "Drive alongside him.":
                cage "Hey. Dirtbag."
            "Keep your distance.":
                "Cage begins snaking back in forth, dodging invisible obstacles, and pulls away laughing."
                cage "Ahahaha!"
                hide cage_sprite
                hide bike
                with moveoutright
                hide racer_sprite with moveoutleft
                return
            "DRIFT!":
                "You drift skillfully towards Nicolas Cage."
                cage "Everything we do impacts someone else's life."
    else:
        # Nic Cage is behind
        show racer_sprite at right with moveinright

        "Nicolas Cage begins approaching from behind."
        show cage_sprite at left
        show bike at left
        with moveinleft

        "He's gaining ground quickly, despite... weaving back and forth,
 gliding his fingers along the ground on each side."

        menu:
            "Cut him off.":
                "Your car swerves suddenly towards the oncoming Cage, but he's faster."
                cage "Hahaha. I love pressure. I eat it for breakfast." 
            "Focus straight ahead.":
                "You feel a tap on the shoulder."
                cage "Every great story seems to begin with a snake."
            "DRIFT!":
                "You skillfully drift down the track."
                "Without skipping a beat, Cage matches your drift."

    "You're neck and neck with Nicolas Cage."

    menu:
        "Run him off the road.":
            jump cage_bees_2
        "Speed past him.":
            "You leave Cage in your tracks and race forward."
            hide cage_sprite
            hide bike
            with moveoutleft
            hide racer_sprite with moveoutright

            if pos_diff < 0:
                $ gamestate.changeStanding('racer', -1)

            return
        "DRIFT!":
            "You begin to slide right at Cage."
            jump cage_bees_2

label cage_bees_2:
    "Cage tries to avoid being hit and angles towards the edge of the track."
    "He turns to stare you down, but is immediately hit by a beehive hanging from a tree."
    cage "OH, NO! NOT THE BEES! NOT THE BEES! AAAAAHHHHH!"
    cage "OH, THEY'RE IN MY EYES! MY EYES! AAAAHHHHH! AAAAAGGHHH!"

    # TODO: Do slight damage to Cage

    hide cage_sprite
    hide bike
    with moveoutleft
    hide racer_sprite with moveoutright

    $ pos_diff = gamestate.position_diff('cage', 'racer')
    if pos_diff < 0:
        $ gamestate.changeStanding('racer', -1)

    return
