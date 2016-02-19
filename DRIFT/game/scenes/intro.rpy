# intro scene
# Introduce Racer and the other Drivers, get a few chances to make some early friends and enemies

init:
    image bg start = "scene_start.png"

label start_intro:
    $racer = gamestate.actors['racer']
    $shiny = gamestate.actors['shiny']
    $chrome = gamestate.actors['chrome']
    $cherry = gamestate.actors['cherry']
    $cage = gamestate.actors['cage']
    $tanaka = gamestate.actors['tanaka']
    $cornelius = gamestate.actors['cornelius']
    $driver = gamestate.actors['driver']

    scene bg start
    announcer "It's finally time!  The DRIFT Championship trials are about to begin!  The drivers are doing the final checks, and we'll be ready to go soon, folks!"

    show racer_sprite at right
    "Now's your chance to check out your competition."

    show v8_interceptor at left
    racer "..."
    show shiny_and_chrome_sprite at left with fade
    shiny "Ready."
    chrome "Good.  You drive, I'll shoot?"
    shiny "Hnh."
    "They seem to be ignoring you."
    menu:
        "Tap on their car.":
            chrome "What?"
            racer "..."
            shiny "..."
            racer "..."
            shiny "Hnh."
            chrome "If you don't have anything to say, leave."
            hide shiny_and_chrome_sprite with moveoutright
        "DRIFT!":
            hide racer_sprite with moveoutright
            hide shiny_and_chrome_sprite with moveoutleft
            show racer_sprite at right
    jump meet_cherry

label meet_cherry:
    show gokart at left
    show cherry_sprite at left
    with moveinleft
    cherry "Hi!  I'm Cherry!"
    menu:
        "Nod.":
            #TODO: Reduce cherry disposition a little
            jump meet_cherry_end
        "Salute.":
            #TODO: Increase cherry disposition
            cherry "There's no need for that.  Out there you are my subjects, but here we're all racers."
            cherry "I haven't seen you before.  Is this your first race?  Watch out for the bus driver."
            jump meet_cherry_end
        "Shrug.":
            #TODO: Reduce cherry disposition moderately
            cherry "Cherry Carter?  The princess?  My face is on the money?"
            jump meet_cherry_end
        "DRIFT!":
            #TODO: Reduce cherry disposition a lot.  She really doesn't like to be ignored.
            hide racer_sprite with moveoutright
            cherry "Ignoring my greeting?  I'm going to DESTROY that driver."
            hide gokart
            hide cherry_sprite
            with moveoutleft
            show racer_sprite at right
            jump meet_cage

label meet_cherry_end:
    cherry "Nice to meet you, racer.  Good luck!"
    cherry "Not that luck will be enough to beat me."
    hide gokart
    hide cherry_sprite
    with moveoutright
    jump meet_cage

label meet_cage:
    show bike
    show cage_sprite
    with moveinleft
    cage "Oh, a fan!  Here, let me sign you an autograph."
    racer "..."
    cage "Surprised?  I know what it's like to meet someone you admire and have them be a complete jerk."
    racer "..."
    cage "Why am I, Nicolas Cage, driving a motorcycle in this extremely dangerous race?  Good question."
    cage "When I was eight, I would look at the cover of the 'Ghost Rider' comic book in my little home in Long Beach, California, and I couldn't get my head around how something that scary could also be good. To me it was my first philosophical awakening - 'How is this possible, this duality?'"
    cage "I think it's no secret that I've tried to take chances in my career and also in my life, and I believe to not live in fear."
    cage "One of the things that's interesting to me is I find things like caffeine and stunts actually relax me. When they're putting a bit of gel on my arm and lighting me on fire, or when I'm about to go into a high-speed car chase or rev a motorcycle up pretty fast, I find everything else around me slows down."
    cage "I am not a demon. I am a lizard, a shark, a heat-seeking panther. I want to be Bob Denver on acid playing the accordion."
    "He's monologuing so intently he doesn't seem to know you're still there.  You should move on."
    hide bike
    hide cage_sprite
    with moveoutright
    jump meet_tanaka

label meet_tanaka:
    show prius at left
    show tanaka_sprite at left
    with moveinleft
    tanaka "A new racer?  I'm Tanaka.  Welcome to DRIFT.  Are you ready?"
    menu:
        "Nod.":
            #TODO: +disposition
            tanaka "Good.  It's more fun to beat somebody at the top of their game."
        "Shake your head."
            #TODO: -disposition
            tanaka "Then you'd better get ready fast.  The race is about to start."
        "DRIFT!"
            #TODO: -disposition
            hide racer_sprite with moveoutright
            tanaka "Hey, don't just ignore me!"
            hide prius
            hide tanaka_sprite
            with moveoutleft
            show racer_sprite at right
            jump meet_cornelius
    hide prius
    hide tanaka_sprite
    with moveoutright
    jump meet_cornelius

label meet_cornelius:
    show electric at left
    show cornelius_sprite at left
    with moveinleft
    cornelius "Ah, a new challenger!  This will be good fun!  I am Cornelius Vandergraaf, of course."
    menu:
        "Shake his hand.":
            #TODO: +disposition
            cornelius "Let's have a good, clean race out there!"
            cornelius "Don't worry, if you come in second, I'll let you have the prize money.  It's just pennies anyway!  But I get the trophy."
        "Nod.":
            #TODO: +disposition
            cornelius "Driver of few words, eh?  I like that!  If you need a job driving trains after I beat you, let's talk after the race!"
        "DRIFT!":
            #TODO: -disposition
            hide racer_sprite with moveoutright
            cornelius "How rude."
            hide electric
            hide cornelius_sprite
            with moveoutleft
            show racer_sprite at right
            jump meet_driver
    hide electric
    hide cornelius_sprite
    with moveoutright
    jump meet_driver

label meet_driver:
    show bus at left
    with moveinleft
    "... is that a schoolbus?"
    #TODO content
    "No time to investigate.  The race is about to start!"
    hide bus
    with moveoutleft
    jump intro_end

label intro_end:
    announcer "Looks like it's time to start!  We've got an all-star lineup tonight - you don't want to miss it!"
    "The crowd cheers as you hurry back to your car.  It's finally time!"
