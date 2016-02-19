# The game starts here.

init python:
    import math

    the_fucking_road = None

    class RoadSurface(renpy.Displayable):

        def __init__(self, width, height, **kwargs):
            # With apologies, we need to be able to keep track of our road
            # as a Python object which Renpy doesn't make easy.
            global the_fucking_road
            the_fucking_road = self

            super(RoadSurface, self).__init__(**kwargs)

            self.width = width
            self.height = height
            self.speed = 0.0
            self.tick = 0.0
            self.last_at = 0.0
            self.rate = 0.0

            self.event_start = 0.0
            self.start = 0.0
            self.event_length = 0.0
            self.destination = 0.0
            self.event_start = 0.0

            self.events = []

        def reset(self):
            self.speed = 0.0
            self.tick = 0.0
            self.last_at = 0.0
            self.rate = 0.0

            self.event_start = 0.0
            self.start = 0.0
            self.event_length = 0.0
            self.destination = 0.0
            self.event_start = 0.0

            self.events = []

        def on_tick(self, index):
            tick_scale = 1.0
            tick_mod = self.tick % tick_scale
            divs = 4
            scale = 1
            while scale < divs:
                if tick_mod < (scale * tick_scale / float(divs)): return (index + (scale - 1)) % divs
                scale += 1
            return (index + (scale - 1)) % divs

        def is_alt_palette(self, i):
            ddz = 0.005
            dz  = 0.005
            z   = 0.0
            while z < 1.0:
                if i < z: return self.on_tick(3),z
                dz += ddz
                z += dz
                if i < z: return self.on_tick(2),z
                dz += ddz
                z += dz
                if i < z: return self.on_tick(1),z
                dz += ddz
                z += dz
                if i < z: return self.on_tick(0),z
                dz += ddz
                z += dz
            return self.on_tick(3),z

        def width_at(self, i):
            return i * 600 + 30

        def curve_at(self, i, curve_rate):
            if abs(curve_rate) < 0.0001: return 0
            return (curve_rate / abs(curve_rate)) * ((1.0 - i) * abs(curve_rate) * ((1.0 - i) * abs(curve_rate) + 1) / 2)

        def render(self, width, height, st, at):
            self.tick += (at - self.last_at) * self.speed
            self.last_at = at
            render = renpy.Render(self.width, self.height)
            c = render.canvas()
            c.rect((133,223,255),(0,0,self.width,self.height/2))

            if self.tick - self.event_start < self.event_length:
                def ease(t,b,c):
                    return c * t + b
                self.rate = ease((self.tick - self.event_start) / self.event_length, self.start, self.destination - self.start)
            else:
                if self.event_length:
                    self.rate = self.destination
                    self.event_length = 0
                # Update curve rate from queued events.
                if self.events:
                    event = self.events.pop(0)
                    self.event_start = self.tick
                    self.start = self.rate
                    if event == "left":
                        self.destination = -25.0
                        self.event_length = 5.0
                    if event == "right":
                        self.destination = 25.0
                        self.event_length = 5.0
                    if event == "straight":
                        self.destination = 0.0
                        self.event_length = 5.0

            for i in range(self.height/2,self.height):
                m = float(i-self.height/2) / float(self.height/2)
                # Grass
                grass = (66,131,0)
                road  = (100,100,100)
                alt   = (255,255,255)
                lane  = (100,100,100)
                w = self.width_at(m)
                x,z = self.is_alt_palette(m)
                if x >= 2:
                    grass = (44,110,0)
                    alt   = (255,0,0)
                    lane  = (255,255,255)
                c.rect(grass,(0,i,self.width,1))
                c.rect(road,(self.curve_at(m, self.rate) + (self.width  - w) / 2,i,w,1))
                c.rect(alt, (self.curve_at(m, self.rate) + (self.width  - w) / 2 - w * 0.05,i,w*0.05,1))
                c.rect(alt, (self.curve_at(m, self.rate) + (self.width  - w) / 2 + w,i,w*0.05,1))
                c.rect(lane,(self.curve_at(m, self.rate) + (self.width  - w * 0.05) / 2,i,w*0.05,1))
            renpy.redraw(self, 0.01)
            return render

image road_surface = RoadSurface(800,600)


label start:
    show road_surface:
        xalign 0.5
        yalign 0.5

    $ the_fucking_road.reset()

    call start_intro

    "3"
    "2"
    "1"

    $ the_fucking_road.speed = 5.0

    call race
    show text str(gamestate.standings)

    $ the_fucking_road.speed = 0.0

    "It's over."
    $ finalPos = gamestate.racers['racer'].getPosition() + 1
    $ worstPos = len(gamestate.standings)
    if finalPos == 1:
        "YOUR WINNER"
    elif finalPos == worstPos:
        "You came in last.  Nicolas Cage is disappointed in you."
    else:
        "You came in position [finalPos].  Try harder next time."
    # TODO: call epilogue
