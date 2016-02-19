# main race loop

init python:
    from random import randint

    def selectEvent():
        return renpy.random.choice([
            e for e in gamestate.events if e.isValid()
        ]).label

    def nextLoc():
        return True

    def raceOver():
        return gamestate.trackIndex >= len(gamestate.track)

    def moveRacersAround():
        skipNext = False
        for i in range(0, len(gamestate.standings)-1):
            if gamestate.standings[i].characterName == 'main' or gamestate.standings[i+1].characterName == 'main' or skipNext:
                skipNext = False
                continue
            passingModifier = 50 - (5 * (gamestate.standings[i].carHealth - gamestate.standings[i+1].carHealth))
            # if they have more health than us, increase their chance of passing us
            if randint(0, 100) < passingModifier:
                gamestate.standings[i].swapPositionWith(gamestate.standings[i+1])
                skipNext = True # don't swap the same racer more than once


label race:
    $ event = selectEvent()

    "Looks like a [event] coming up."
    python:
        if event == 'turn':
            the_fucking_road.events.append('left')
        else:
            the_fucking_road.events.append('straight')
    call expression event
    "Whew, made it past that one."

    python:
        moveRacersAround()
        if nextLoc():
            gamestate.trackIndex += 1

            if raceOver():
                renpy.return_statement()

        renpy.jump("race")
