# main race loop

init python:
    import store.gamestate as gamestate
    
    def selectEvent():
        return "turn"

    def nextLoc():
        return True

    def raceOver():
        return renpy.random.choice([False, True])

label race:
    $ event = selectEvent()

    "Looks like a [event] coming up."
    call expression event
    "Whew, made it past that one."

    python:
        if nextLoc():
            pass  # TODO: increment location here
            if raceOver():
                renpy.return_statement()
        renpy.jump("race")
