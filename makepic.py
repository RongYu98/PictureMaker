globvar = 0

def doSomething( num ):
    global globvar
    num = num + globvar
    globvar += 1
    return num % 255

def color():
    fil = open("pic.ppm", "w")
    fil.write("P3 200 200 255 ")
    print("[P3 200 200 255 ]")
    r = 0
    g = 0
    b = 255
    i = 0
    while (r < 200):
        red = doSomething( r )
        g = 0
        while (g < 200):
            green = doSomething( g )
            fil.write( "%d %d %d " % ( red, green, b ) )
            #print("[%d %d %d ]" % ( red, green, b ))
            g += 1
        r += 1
    fil.close()

color()
print globvar