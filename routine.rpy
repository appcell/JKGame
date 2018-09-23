




label routine_start:


    show screen monologue()

    python:
        store.update()


    show jotaro normal
    jotaro "收养的事情怎么样了？"
    hide jotaro

    if store.continue_routine is True:
        menu:
            "上课":
                python:
                    intimacy += 3
                    health -= 10
                    day += 1

            "休息":
                python:
                    intimacy += 3
                    health += 20
                    day += 1


            "去找dio放飞自我":
                python:
                    intimacy -= 5
                    health += 20
                    day += 1



    if day > 10:
        hide screen monologue
        return


    jump routine_start


    
