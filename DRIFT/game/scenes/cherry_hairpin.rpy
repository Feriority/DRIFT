# Event when near cherry

init 1 python:
    import store.gamestate as gamestate

    class CherryHairpinEvent(classes.Event):
        def isValid(self):
            return gamestate.are_adjacent('cherry', 'racer') and gamestate.track[gamestate.trackIndex] == 'turn'

    CherryHairpinEvent('cherry_hairpin')


label cherry_hairpin:
    show racer_sprite at right with moveinleft
    "You're coming up on a series of sharp turns snaking down a steep hill, followed by a tight hairpin."
    show gokart at left
    show cherry_sprite at left
    with moveinright
    $ pos_diff = gamestate.position_diff('cherry', 'racer')
    if pos_diff < 0:
        # Cherry is in front
        "You can see Princess Cherry ahead of you on her gokart."
    else:
        "You can see Princess Cherry gaining on you on her gokart."

    menu:
        "Speed up!":
            $ success = renpy.random.random()
            if success >= 0.80:
                "You hit the turns fast, but corner perfectly.  You're almost at the bottom now, and ahead of the princess, who drifted her way down but couldn't match your speed."
                if pos_diff < 0:
                    $ gamestate.changeStanding('racer', -1)
            elif success >= 0.60:
                "You hit the turns fast, but corner perfectly.  You're almost at the bottom now, and neck and neck with the princess, who drifted her way down in a flash of blue sparks."
            else:
                "You speed into the turns and drive straight off the road, crashing into a tree.  Your car explodes."
                $ gamestate.changeStanding('racer', 2)
                hide racer_sprite with vpunch
                hide gokart
                hide cherry_sprite
                with moveoutright
                return
        "Take the turns carefully.":
            if pos_diff < 0:
                "You carefully maneuver down the slope and through the hairpin.  Nobody passes you, but Princess Cherry skillfully drifts through the curves and increases her lead."
                hide racer_sprite
                hide gokart
                hide cherry_sprite
                with moveoutright
                return
            else:
                "You carefully maneuver down the slope.  Princess Cherry's adept drifting lets her take the turns faster than you, and by the time you reach the hairpin, you're neck and neck."
        "DRIFT!":
            "You and the princess drift your way through the snaking road, her gokart's tires throwing blue sparks at every turn.  You make it to the bottom neck and neck."

    "All that's left is the hairpin.  As you approach it, the princess throws a banana peel at your car.  It's not very effective."
    menu:
        "Full speed ahead!":
            "You drive straight, and the road turns.  Your offroading skills are commendable, but they won't actually help much in this race."
            $ gamestate.changeStanding('racer', 1)
        "Go slow.":
            "Cherry drifts the hairpin while you take it slow.  As she pulls ahead, she waves and smiles from her gokart."
            $ disp = gamestate.racers['cherry'].disposition
            if disp > 0:
                cherry "See you at the finish line!"
            else:
                cherry "BOW BEFORE YOUR PRINCESS!"
            if pos_diff > 0:
                $ gamestate.changeStanding('racer', 1)
        "Ram her!":
            # Cherry does not take kindly to your attempt
            $ gamestate.racers['cherry'].changeDisposition(-20)
            $ success = renpy.random.random()
            if success >= 0.66:
                "You're driving a car.  Cherry is driving a gokart.  The math is not difficult."
                hide cherry_sprite
                hide gokart with vpunch
                $ gamestate.changeStanding('cherry', 2)
            elif success >= 0.33:
                "You're driving a car.  Cherry is driving a gokart.  The math is not difficult.  Keeping control of your car on a hairpin while ramming someone, however, is.  You both careen off the road and explode."
                if pos_diff < 0:
                    $ gamestate.changeStanding('racer', -1)
                $ gamestate.changeStanding('cherry', 2)
                $ gamestate.changeStanding('racer', 2)
                hide cherry_sprite
                hide gokart with vpunch
                hide racer_sprite with hpunch
            else:
                "You're driving a car.  Cherry is driving a gokart.  The math is not - wait, is that a star?  Why is she glowing random colors?"
                hide racer_sprite with vpunch
                "You're not sure WHY your car exploded, but you probably deserved it."
                $ gamestate.changeStanding('racer', 2)
        "DRIFT!":
            $ success = renpy.random.random()
            if success >= 0.60:
                "You two drift around the hairpin, so close your vehicles are almost touching.  Then your car slides and knocks her little gokart off the road.  Whatever the princess is about to say is cut off by the explosion."
                hide cherry_sprite
                hide gokart with vpunch
                $ gamestate.changeStanding('cherry', 2)
            elif success >= 0.20:
                "You two drift around the hairpin, so close your vehicles are almost touching.  Cherry takes a bite out of a massive mushroom, but as she boosts ahead, her gokart bounces off your car on the outside of the turn, and she loses her speed trying to hold position."
                if pos_diff < 0:
                    $ gamestate.changeStanding('racer', -1)
            else:
                "You two drift around the hairpin, so close your vehicles are almost touching.  Cherry takes a bite out of a massive mushroom, bounces her gokart off your car on the inside of the turn, and boosts ahead in a sudden burst of speed."
            if pos_diff > 0:
                $ gamestate.changeStanding('racer', 1)
    hide racer_sprite
    hide gokart
    hide cherry_sprite
    with moveoutright
