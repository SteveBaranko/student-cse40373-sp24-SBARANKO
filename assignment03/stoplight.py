from sense_hat import SenseHat
import time

s = SenseHat()

dim_green = (0, 10, 0)
brighter_green = (0, 255, 0)
dim_weird_green = (10, 0, 0)
weird_green = (0, 255, 0)
dim_yellow = (10, 10, 0)
brighter_yellow = (255, 255, 0)
dim_red = (10, 0, 0)
brighter_red = (255, 0, 0)
nothing = (0,0,0)

north_south = True



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
        O, O, O, g, g, O, O, O,
        O, O, O, y, y, O, O, O,
        O, O, O, W, r, O, O, O,
        g, y, R, O, O, R, y, g,
        g, y, R, O, O, R, y, g,
        O, O, O, r, W, O, O, O,
        O, O, O, y, y, O, O, O,
        O, O, O, g, g, O, O, O,
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
        O, O, O, G, G, O, O, O,
        O, O, O, y, y, O, O, O,
        O, O, O, w, r, O, O, O,
        g, y, R, O, O, R, y, g,
        g, y, R, O, O, R, y, g,
        O, O, O, r, w, O, O, O,
        O, O, O, y, y, O, O, O,
        O, O, O, G, G, O, O, O,
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
    #yellow light for north south
    #red light for east west
    return [
        O, O, O, g, g, O, O, O,
        O, O, O, Y, Y, O, O, O,
        O, O, O, w, r, O, O, O,
        g, y, R, O, O, R, y, g,
        g, y, R, O, O, R, y, g,
        O, O, O, r, w, O, O, O,
        O, O, O, Y, Y, O, O, O,
        O, O, O, g, g, O, O, O,
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
        O, O, O, g, g, O, O, O,
        O, O, O, y, y, O, O, O,
        O, O, O, R, R, O, O, O,
        g, y, W, O, O, r, y, g,
        g, y, r, O, O, W, y, g,
        O, O, O, R, R, O, O, O,
        O, O, O, y, y, O, O, O,
        O, O, O, g, g, O, O, O,
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
        O, O, O, g, g, O, O, O,
        O, O, O, y, y, O, O, O,
        O, O, O, R, R, O, O, O,
        G, y, r, O, O, r, y, G,
        G, y, r, O, O, r, y, G,
        O, O, O, R, R, O, O, O,
        O, O, O, y, y, O, O, O,
        O, O, O, g, g, O, O, O,
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
        O, O, O, g, g, O, O, O,
        O, O, O, y, y, O, O, O,
        O, O, O, R, R, O, O, O,
        g, Y, r, O, O, r, Y, g,
        g, Y, r, O, O, r, Y, g,
        O, O, O, R, R, O, O, O,
        O, O, O, y, y, O, O, O,
        O, O, O, g, g, O, O, O,
    ]


count = 0
while True:
    s.set_pixels(state1())
    time.sleep(3)
    s.set_pixels(state2())
    time.sleep(5)
    s.set_pixels(state3())
    time.sleep(1)
    s.set_pixels(state4())
    time.sleep(3)
    s.set_pixels(state5())
    time.sleep(5)
    s.set_pixels(state6())
    time.sleep(1)
    count += 1

      