

# Characters

define jotaro = Character('空条 承太郎', color="#c8ffc8")
define jotaro_nvl = Character(kind = nvl, color="#c8ffc8")
define secretary = Character('秘书', color="#c8ffc8")
define robber = Character('绑架犯', color="#c8ffc8")
define unknown = Character('???', color="#999999")
define kakyoin = Character('花京院 典明', color="#c8c8ff")


# Transitions

define fadehold = Fade(0.7, 1.0, 0.7)
define fadelong = Fade(0.7, 3.0, 0.7)

# intermediate flags


# Persistant variables


init python in numerics:
    store.continue_routine = True
    store.intimacy = 0
    store.health = 500
    store.day = 1

    def update():
        store.intimacy += 20
        if store.day > 5:
            store.continue_routine = False

