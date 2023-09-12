def initial_state():
    return (8, 0, 0)

def is_goal(s):
    if(s[0] == 4 and s[1] == 4):
        return True
    else:
        return False

def successors(s):
    x, y, z = s
    #empty one bottle
    if x>0:
        yield((0,y,z),x)
    if y>0:
        yield((x,0,z),y)
    if z>0:
        yield((x,y,0),z)
    #fill one botle
    if x<8:
        yield((8,y,z),8-x)
    if y<5:
        yield((x,5,z),5-y)
    if z<3:
        yield((x,y,3),3-z)
        
    #pour x to y
    t = 5-y
    if x>0 and t > 0:
        if x > t:
            yield ((x-t,5,z), t)
        else:
            yield ((0,x+y,z), x)
    #pour y to x
    t = 8-x
    if y>0 and t > 0:
        if y > t:
            yield ((8,y-t,z), t)
        else:
            yield ((y+x,0,z), y)
    #pour x to z
    t = 3-z
    if x>0 and t > 0:
        if x > t:
            yield ((x-t,y,3), t)
        else:
            yield ((0,y,z+x), x)
    #pour z to x
    t = 8-x
    if z>0 and t > 0:
        if z > t:
            yield ((8,y,z-t), t)
        else:
            yield ((x+z,y,0), x)
    #pour z to y
    t = 5-y
    if z>0 and t>0:
        if z > t:
            yield ((x,5,z-t), t)
        else:
            yield ((x,y+z,0), z)
    #pour y to z
    t = 3-z
    if y>0 and t > 0:
        if y > t:
            yield ((x,y-t,3), t)
        else:
            yield ((x,0,z+y), y)
