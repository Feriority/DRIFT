# The game starts here.

init python:
    import math

    the_fucking_road = None

    class RoadSurface(renpy.Displayable):

        def __init__(self, width, height, **kwargs):
            global the_fucking_road
            the_fucking_road = self
            super(RoadSurface, self).__init__(**kwargs)
            self.width = width
            self.height = height
            self.speed = 0.0
            self.tick = 0.0
            self.last_at = 0.0

        def render(self, width, height, st, at):
            self.tick += (at - self.last_at) * self.speed
            self.last_at = at
            render = renpy.Render(self.width, self.height)
            c = render.canvas()
            c.rect((133,223,255),(0,0,self.width,self.height/2))
            for i in range(self.height/2,self.height):
                m = 1.0 - float(self.height-i) / float(self.height)
                c.rect((66*m,131*m,0*m),(0,i,self.width,1))
            c.circle((255,0,0),(self.width/2,self.height/2),200 + 100 * math.sin(self.tick),0)
            renpy.redraw(self, 0.01)
            return render

image road_surface = RoadSurface(800,600)


label start:
    show road_surface:
        xalign 0.5
        yalign 0.5
        0.2
        repeat

    "It was the day of the Race."
    # TODO: call prologue

    "3"
    "2"
    "1"

    $ the_fucking_road.speed = 5.0

    call race

    $ the_fucking_road.speed = 0.0

    "It's over."
    # TODO: call epilogue
