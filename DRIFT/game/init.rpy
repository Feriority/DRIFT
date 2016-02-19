# This file initalizes all of our game state objects

#

init python in gamestate:

    standings = [] # standings in the race
    track = [] # list of strings that make up the current track
    trackIndex = 0 # current index in the track
    events = []

init python in classes:
    import store.gamestate as gamestate
    # Class defines a single racer character
    class Racer:
        def __init__(self, characterName='Test'):
            self.characterName = characterName
            self.carHealth = 10
            self.disposition = 5
            gamestate.standings.append(self)
    
        def __str__(self):
            return self.characterName
    
    class Event:
        def __init__(self, label):
            self.label = label
            gamestate.events.append(self)
    
        def isValid(self):
            return True
    
    # sample events
    class StraightawayEvent(Event):
        def isValid(self):
            return gamestate.track[gamestate.trackIndex] == 'straightaway'

    class TurnEvent(Event):
        def isValid(self):
            return gamestate.track[gamestate.trackIndex] == 'turn'

init python:
    import store.classes as classes
    
    # TODO SECTION: Make actual shit, not mock shit
    # Initalize 7 sample racers
    for i in range(0, 7):
        classes.Racer(characterName='Test Racer' + str(i))

    for i in range(0, 5):
        gamestate.track.append('straightaway')
        gamestate.track.append('turn')
