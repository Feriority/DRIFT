# main race loop

init python:
    def selectEvent():
        return renpy.random.choice([
            e for e in gamestate.events if e.isValid(gamestate)
        ]).label

    def nextLoc():
        return True

    def raceOver():
        return gamestate.trackIndex >= len(gamestate.track)

label race:
    $ event = selectEvent()

    "Looks like a [event] coming up."
    call expression event
    "Whew, made it past that one."

    python:
        if nextLoc():
            gamestate.trackIndex += 1

            if raceOver():
                renpy.return_statement()

        renpy.jump("race")
