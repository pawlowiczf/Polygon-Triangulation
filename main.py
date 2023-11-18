from createPolygon import createPolygon
from visualizer.main import Visualizer 
from triangulation import earClippingAlgorithm
from triangulationGIF import earClippingAlgorithmGIF

def triangulatePolygon():
    #
    polygon1 = createPolygon()
    polygon2 = polygon1[:]

    vis = Visualizer()
    vis.clear()
    vis.axis_equal()

    visGIF = Visualizer()
    visGIF.clear()
    visGIF.axis_equal()

    vis    = earClippingAlgorithm(polygon1, vis)
    visGIF = earClippingAlgorithmGIF(polygon2, visGIF)

    vis.add_title("Polygon triangulation")
    visGIF.add_title("Polygon triangulation - GIF")
    
    return vis, visGIF
#end procedure triangulatePolygon()

# To show triangulation:
vis, visGIF = triangulatePolygon()
vis.show()

# To save GIF file:
# visGIF.save_gif("polygonTriangulation", interval = 750)
