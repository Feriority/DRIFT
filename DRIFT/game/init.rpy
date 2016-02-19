# This file initalizes all of our game state objects

#

init python in gamestate:

    standings = [] # standings in the race
    track = [] # list of strings that make up the current track
    trackIndex = 0 # current index in the track
    events = []
    
    # Class defines a single racer character
    class Racer:
        def __init__(self, characterName='Test'):
            self.characterName = characterName
            self.carHealth = 10
            self.disposition = 5
            standings.append(self)
    
        def __str__(self):
            return self.characterName
    
    class ActionEvent:
        
        def __init__(self, label):
            self.label = label
            events.append(self)
    
        def isValid(self, gamestate): pass
    
    # sample event
    class TestEventOne(ActionEvent):
        def isValid(self, gamestate):
            return gamestate.track[gamestate.trackIndex] == 'straightaway'

    class TestEventTwo(ActionEvent):
        def isValid(self, gamestate):
            return gamestate.track[gamestate.trackIndex] == 'turn'
    
    # TODO SECTION: Make actual shit, not mock shit
    # Initalize 7 sample racers
    for i in range(0, 7):
        Racer(characterName='Test Racer' + str(i))

    for i in range(0, 5):
        track.append('straightaway')
        track.append('turn')



init python:
    import store.gamestate as gamestate