label winner_cherry:
    $ cherry = gamestate.actors['cherry']
    show cherry_sprite with fade
    cherry "Oh... did I win?"
    cherry "Just kidding.  Of course I won!"
    hide cherry_sprite with fade
    return

label winner_shinychrome:
    $ shiny = gamestate.actors['shiny']
    $ chrome = gamestate.actors['chrome']
    show shiny_and_chrome_sprite with fade
    shiny "Hnh."
    chrome "This was nothing, after driving the Angry Avenue."
    shiny "Good."
    hide shiny_and_chrome_sprite with fade
    return

label winner_cage:
    $ cage = gamestate.actors['cage']
    show cage_sprite with fade
    cage "I try not to be proud. I try to actively attack pride."
    cage "I think what makes people fascinating is conflict, it's drama, it's the human condition. Nobody wants to watch perfection."
    cage "I was always shocked when I went to the doctor's office and they did my X-ray and didn't find that I had eight more ribs than I should have or that my blood was the color green."
    cage "I don't want to sit around by the pool luxuriating with a margarita. That's just not what I want to do."
    "His speech continues for several minutes."
    hide cage_sprite with fade
    return

label winner_tanaka:
    $ tanaka = gamestate.actors['tanaka']
    show tanaka_sprite with fade
    tanaka "I won?  Coo.  I mean, cool."
    tanaka "I'm not a bird."
    hide tanaka_sprite with fade
    return

label winner_cornelius:
    $ cornelius = gamestate.actors['cornelius']
    show cornelius_sprite with fade
    cornelius "Victory!  It's no surprise, really.  You were no match for me."
    cornelius "Just a reminder that Vandergraaf Railways and Vandergraaf Heavy Industries are hiring!  We could use good drivers, but we'll settle for you, ha ha."
    hide cornelius_sprite with fade
    return

label winner_driver:
    $ driver = gamestate.actors['driver']
    show bus with fade
    driver "AHAHAHAHAHAHAHAHAHAHA"
    "The bus passengers bang on the windows.  It doesn't seem to do them any good."
    hide bus with fade
    return
