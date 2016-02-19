# straightaway scene
# currently this is only an example for testing purposes

init 1 python:
    import store.gamestate as gamestate
    gamestate.StraightawayEvent("straightaway")

label straightaway:
    "On a straightaway."
    return
