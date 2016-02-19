# main race loop

init python:
    def selectEvent():
        event = renpy.random.choice([
            e for e in gamestate.events if e.isValid()
        ])
        if event.play_once_only:
            gamestate.events.remove(event)
        return event.label

    def nextLoc():
        return True

    def raceOver():
        return gamestate.trackIndex >= len(gamestate.track)

    def moveRacersAround():
        skipNext = False
        for i, racer in enumerate(gamestate.standings):
            if i+1 >= len(gamestate.standings):
                break

            other_racer = gamestate.standings[i+1]
            if racer.characterName == 'Racer' or other_racer.characterName == 'Racer' or skipNext:
                skipNext = False
                continue

            passingModifier = 50 - (5 * (racer.carHealth - other_racer.carHealth))
            # if they have more health than us, increase their chance of passing us
            if renpy.random.randint(0, 100) < passingModifier:
                racer.swapPositionWith(other_racer)
                skipNext = True  # don't swap the same racer more than once


label race:
    show text str(gamestate.standings)
    
    $ location = gamestate.track[gamestate.trackIndex]
    $ event = selectEvent()

    python:
        if location == 'turn':
            the_fucking_road.events.append('left')
        else:
            the_fucking_road.events.append('straight')
    call expression event

    python:
        moveRacersAround()
        if nextLoc():
            gamestate.trackIndex += 1

            if raceOver():
                renpy.return_statement()

        renpy.jump("race")
