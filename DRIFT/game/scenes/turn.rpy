# turn scene
# currently this is only an example for testing purposes

init 1 python:
    import store.gamestate as gamestate
    gamestate.TurnEvent("turn")

label turn:
    "On a turn."
    return
