# This file initalizes all of our game state objects

#

init python in gamestate:

    standings = [] # standings in the race
    track = [] # list of strings that make up the current track
    trackIndex = 0 # current index in the track
    events = set()
    racers = {}
    actors = {}

    def changeStanding(racer, diff):
        if isinstance(racer, basestring):
            racer = racers[racer]
        racer_standing = racer.getPosition()

        standings.pop(racer_standing)

        new_standing = racer_standing + diff
        if new_standing < 0:
            new_standing = 0

        if new_standing > len(standings):
            new_standing = len(standings)

        standings.insert(new_standing, racer)

    def position_diff(racer1, racer2):
        racer1_index = racers[racer1].getPosition()
        racer2_index = racers[racer2].getPosition()
        return racer1_index - racer2_index

    def are_adjacent(racer1, racer2):
        return abs(position_diff(racer1, racer2)) <= 1

    def getRacerAt(position):
        if position < 0:
            return None

        if position >= len(standings):
            return None

        return standings[position]

init python in classes:
    import store.gamestate as gamestate
    # Class defines a single racer character
    class Racer:
        def __init__(self, characterName='Test', characterKey='Test'):
            self.characterName = characterName
            self.carHealth = 10
            self.disposition = 0
            self.key = characterKey
            gamestate.standings.append(self)
            self.actor = renpy.character.Character(characterName)
            gamestate.racers[characterKey] = self
            gamestate.actors[characterKey] = self.actor
    
        def getPosition(self):
            """get 0 indexed position in race"""
            return gamestate.standings.index(self)

        def swapPositionWith(self, racer):
            myPosition = self.getPosition()
            theirPosition = racer.getPosition()
            gamestate.standings[myPosition], gamestate.standings[theirPosition] = racer, self

        def changeDisposition(self, diff):
            self.disposition += diff

            if self.disposition > 10:
                self.disposition = 10

            if self.disposition < -10:
                self.disposition = -10

        def __repr__(self):
            return self.characterName

    class Event:
        play_once_only = True

        def __init__(self, label):
            self.label = label
            gamestate.events.add(self)
    
        def isValid(self):
            return True
    
    # sample events
    class StraightawayEvent(Event):
        # Simple events are repeatable
        play_once_only = False

        def isValid(self):
            return gamestate.track[gamestate.trackIndex] == 'straightaway'

    class TurnEvent(Event):
        # Simple events are repeatable
        play_once_only = False

        def isValid(self):
            return gamestate.track[gamestate.trackIndex] == 'turn'


init python:
    import store.classes as classes
    
    # Initalize 7 sample racers
    classes.Racer(characterName='Shiny and Chrome', characterKey='shinychrome')
    gamestate.actors['shiny'] = renpy.character.Character('Shiny')
    gamestate.actors['chrome'] = renpy.character.Character('Chrome')

    classes.Racer(characterName='Princess Cherry Carter', characterKey='cherry')
    classes.Racer(characterName='Nicolas Cage', characterKey='cage')
    classes.Racer(characterName='Tanaka', characterKey='tanaka')
    classes.Racer(characterName='Bus Driver', characterKey='driver')
    classes.Racer(characterName='Cornelius Vandergraaf', characterKey='cornelius')

    # Start racers in random positions
    renpy.random.shuffle(gamestate.standings)
    classes.Racer(characterName='Racer', characterKey='racer')

    for i in range(0, 5):
        gamestate.track.append('straightaway')
        gamestate.track.append('turn')


# Initialize sprites
init:
    image racer_sprite = "racer.png"

    image v8_interceptor = "v8_interceptor.png"
    image shiny_and_chrome_sprite = "shiny_and_chrome.png"

    image gokart = "gokart.png"
    image cherry_sprite = "cherry.png"

    image bike = "bike.png"
    image cage_sprite = "cage.png"

    image prius = "prius.png"
    image tanaka_sprite = "tanaka.png"

    image electric = "electric.png"
    image cornelius_sprite = "cornelius.png"

    image bus = "bus.png"
