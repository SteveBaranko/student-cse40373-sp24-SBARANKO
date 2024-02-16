from sense_hat import SenseHat
import time

s = SenseHat()

dim_green = (0, 10, 0)
brighter_green = (0, 255, 0)
dim_weird_green = (10, 0, 0)
weird_green = (30, 150, 30)
dim_yellow = (10, 10, 0)
brighter_yellow = (255, 255, 0)
dim_red = (10, 0, 0)
brighter_red = (255, 0, 0)
nothing = (0,0,0)

C = brighter_red
NS = brighter_red
EW = brighter_red

'''
  THE STOPLIGHT SHOULD LOOK LIKE THIS 
          return [
        O, O, O, N, N, O, O, O,
        O, O, O, N, N, O, O, O,
        O, O, O, N, N, O, O, O,
        W, W, W, O, O, E, E, E,
        W, W, W, O, O, E, E, E,
        O, O, O, S, S, O, O, O,
        O, O, O, S, S, O, O, O,
        O, O, O, S, S, O, O, O,
    ]
    

'''

def state1():
    g = dim_green
    y = dim_yellow
    R = brighter_red
    r = dim_red
    w = dim_weird_green
    W = weird_green
    O = nothing
    #left arrow for north south
    #red light for east west
    return [
        O, NS, O, g, g, O, NS, O,
        EW, C, O, y, y, O, C, EW,
        O, O, O, W, r, O, O, O,
        g, y, R, O, O, R, y, g,
        g, y, R, O, O, R, y, g,
        O, O, O, r, W, O, O, O,
        EW, C, O, y, y, O, C, EW,
        O, NS, O, g, g, O, NS, O,
    ]
def state2():
    g = dim_green
    G = brighter_green
    y = dim_yellow
    w = dim_weird_green
    r = dim_red
    R = brighter_red
    O = nothing
    #green light for north south
    #red light for east west
    return [
        O, NS, O, G, G, O, NS, O,
        EW, C, O, y, y, O, C, EW,
        O, O, O, w, r, O, O, O,
        g, y, R, O, O, R, y, g,
        g, y, R, O, O, R, y, g,
        O, O, O, r, w, O, O, O,
        EW, C, O, y, y, O, C, EW,
        O, NS, O, G, G, O, NS, O,
    ]
def state3():
    g = dim_green
    y = dim_yellow
    Y = brighter_yellow
    w = dim_weird_green
    W = weird_green
    r = dim_red
    R = brighter_red
    O = nothing
    # yellow light for north south
    # red light for east west
    return [
        O, NS, O, g, g, O, NS, O,
        EW, C, O, Y, Y, O, C, EW,
        O, O, O, r, w, O, O, O,
        g, y, R, O, O, R, y, g,
        g, y, R, O, O, R, y, g,
        O, O, O, w, r, O, O, O,
        EW, C, O, Y, Y, O, C, EW,
        O, NS, O, g, g, O, NS, O,
    ]
def state4():
    G = brighter_green
    g = dim_green
    y = dim_yellow
    r = dim_red
    R = brighter_red
    w = dim_weird_green
    W = weird_green
    O = nothing
    #red light for north south
    #left arrow for east west
    return [
        O, NS, O, g, g, O, NS, O,
        EW, C, O, y, y, O, C, EW,
        O, O, O, R, R, O, O, O,
        g, y, r, O, O, W, y, g,
        g, y, W, O, O, r, y, g,
        O, O, O, R, R, O, O, O,
        EW, C, O, y, y, O, C, EW,
        O, NS, O, g, g, O, NS, O,
    ]
def state5():
    g = dim_green
    G = brighter_green
    y = dim_yellow
    w = dim_weird_green
    r = dim_red
    R = brighter_red
    O = nothing
    #green light for east west
    #red light for north south
    return [
        O, NS, O, g, g, O, NS, O,
        EW, C, O, y, y, O, C, EW,
        O, O, O, R, R, O, O, O,
        G, y, r, O, O, r, y, G,
        G, y, r, O, O, r, y, G,
        O, O, O, R, R, O, O, O,
        EW, C, O, y, y, O, C, EW,
        O, NS, O, g, g, O, NS, O,
    ]
def state6():
    g = dim_green
    y = dim_yellow
    Y = brighter_yellow
    w = dim_weird_green
    W = weird_green
    r = dim_red
    R = brighter_red
    O = nothing
    #yellow light for east west
    #red light for north south
    return [
        O, NS, O, g, g, O, NS, O,
        EW, C, O, y, y, O, C, EW,
        O, O, O, R, R, O, O, O,
        g, Y, r, O, O, r, Y, g,
        g, Y, r, O, O, r, Y, g,
        O, O, O, R, R, O, O, O,
        EW, C, O, y, y, O, C, EW,
        O, NS, O, g, g, O, NS, O,
    ]


def sleep_and_poll(time_s):
    global nsc, ewc

    start_time = time.time()

    try:
        while time.time() - start_time < time_s:
            time.sleep(0.005)  # Sleep for 5 ms (adjust as needed)

            for event in s.stick.get_events():
                if event.action == "pressed":
                    if event.direction in ["up", "down"]:
                        nsc = True
                    elif event.direction in ["left", "right"]:
                        ewc = True
                        
            #if nsc or ewc:
                # just wait
                #pass

    except KeyboardInterrupt:
        pass


nsc = False
ewc = False

state = 0

while True:
    s.set_pixels(state1())
    state = 1
    sleep_and_poll(9.9)
    state = 2
    if(ewc):
        #20 seconds of green, 5 of flashing, then 5 of red for crosswalk
        NS = brighter_green
        C = brighter_green
        s.set_pixels(state2())
        time.sleep(20)
        for i in range(20):
            #blink NS and C red for 5 seconds
            if(i%2 == 0):
                NS = brighter_red
                C = brighter_red
                s.set_pixels(state2())
                time.sleep(.25)
                
            else:
                NS = nothing
                C = nothing
                s.set_pixels(state2())
                time.sleep(.25)
                
        ewc = False
        NS = brighter_red
        C = brighter_red
        s.set_pixels(state2())
        time.sleep(5)
    else:
        s.set_pixels(state2())
        sleep_and_poll(30)
    s.set_pixels(state3())
    state = 3  
    sleep_and_poll(9.9)
    s.set_pixels(state4())
    state = 4
    sleep_and_poll(10)

    state = 5
    if(nsc):
        EW = brighter_green
        C = brighter_green
        s.set_pixels(state5())
        #20 seconds of green, 5 of flashing, then 5 of red for crosswalk
        time.sleep(20)
        # 20 in loop represents 5 seconds of flashing (.25 is sleep time)
        for i in range(20):
            #blink NS and C red for 5 seconds
            if(i%2 == 0):
                EW = brighter_red
                C = brighter_red
                s.set_pixels(state5())
                time.sleep(.25)
            else:
                EW = nothing
                C = nothing
                s.set_pixels(state5())
                time.sleep(.25)
        nsc = False
        EW = brighter_red
        C = brighter_red
        #5 seconds of red for crosswalk
        s.set_pixels(state5())
        time.sleep(5)
    else:
        s.set_pixels(state5())
        sleep_and_poll(30)
    s.set_pixels(state6())
    state = 6
    sleep_and_poll(9.9)