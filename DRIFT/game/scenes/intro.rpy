# intro scene
# Introduce Racer and the other Drivers, get a few chances to make some early friends and enemies

init:
    image bg start = "scene_start.png"
    image racer_sprite = "racer.png"

    image v8_interceptor = "v8_interceptor.png"
    image shiny_and_chrome_sprite = "shiny_and_chrome.png"

    image gokart = "gokart.png"
    image cherry_sprite = "cherry.png"

    image bike = "bike.png"
    image cage_sprite = "cage.png"

    define announcer = Character('Announcer')
    define racer = Character('Racer')
    define shiny = Character('Shiny')
    define chrome = Character('Chrome')
    define cherry = Character('Cherry')
    define cage = Character('Cage')


label start_intro:
    scene bg start
    announcer "It's finally time!  The DRIFT Championship trials are about to begin!  The drivers are doing the final checks, and we'll be ready to go soon, folks!"

    show racer_sprite at right
    "Now's your chance to check out your competition."

    show v8_interceptor at left
    hero "..."
    show shiny_and_chrome_sprite at left with fade
    shiny "Ready."
    chrome "Good.  You drive, I'll shoot?"
    shiny "Hnh."
    "They seem to be ignoring you."
    menu:
        "Tap on their car.":
            jump shiny_and_chrome_intro
        "DRIFT!":
            jump meet_cherry

label shiny_and_chrome_intro:
    chrome "What?"
    hero "..."
    shiny "..."
    hero "..."
    shiny "Hnh."
    chrome "If you don't have anything to say, leave."
    jump meet_cherry

label meet_cherry:
    hide shiny_and_chrome_sprite with moveoutright
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
            jump meet_cage

label meet_cherry_end:
    cherry "Nice to meet you, racer.  Good luck!"
    jump meet_cage

label meet_cage:
    hide gokart
    hide cherry
    with moveoutright
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
    jump meet_tanaka
