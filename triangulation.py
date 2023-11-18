from arrayColors import createLinkedList

def mapArray(polygon):
    #
    for a in range( len(polygon) ):
        #
        coords = polygon[a]
        polygon[a] = ( coords, a )
    #
    
    return polygon
#end procedure mapArray()

def Orientation(A, B, C):
    #
    ax, ay = A 
    bx, by = B 
    cx, cy = C 

    answer = (ax - cx) * (by - cy) - (ay - cy) * (bx - cx)
    return answer
#end procedure Orientation()

def Position(A, B, C):
    #
    ax, ay = A 
    bx, by = B 
    cx, cy = C 

    answer = (ax - cx) * (by - cy) - (ay - cy) * (bx - cx)

    if answer > 0: return 1 
    if answer < 0: return -1
    return float('inf')
#end procedure Orientation()

def inTriangle(pointA, pointB, pointC, pointInside):
    #
    number = 0
    number += Position(pointA, pointB, pointInside)
    number += Position(pointB, pointC, pointInside)
    number += Position(pointC, pointA, pointInside)

    if abs( number ) == 3:
        return True
    #
    return False
#end procedure inTriangle()

def searchForEar(polygon, vis, fillColor):
    #
    n = len(polygon)
    if len(polygon) < 3: return []
    
    for a in range( len(polygon)  ):
        #
        pointA = polygon[ (a - 1) % n ][0]
        pointB = polygon[ a % n ][0]
        pointC = polygon[ (a + 1) % n ][0]

        if Orientation(pointA, pointB, pointC) > 0:
            flag = True 

            for pointInside, index in polygon:
                if not ( pointInside in (pointA, pointB, pointC) ) and inTriangle(pointA, pointB, pointC, pointInside):
                    flag = False 
                    break
            #

            if flag:    
                pol = [pointA, pointB, pointC]
                vis.add_polygon(pol, color = fillColor.color)
                return ( polygon[ (a - 1) % n ][1], a % n , polygon[ (a + 1) % n ][1] )
        #
    #end 'for' loop 

    return []
#end procedure searchForEar()

def earClippingAlgorithm(polygon, vis):
    #
    if len(polygon) == 0: return []
    
    polygon = mapArray(polygon)
    colors = [ "orange", "red", "green", "purple", "brown", "blue" ]
    fillColor = createLinkedList(colors)
    
    while len(polygon) >= 3:
        #
        index = searchForEar(polygon, vis, fillColor)
        if index == []: break
        polygon.pop( index[1] )
        fillColor = fillColor.next
    #

    return vis
#end procedure earClippingAlgorithm()
