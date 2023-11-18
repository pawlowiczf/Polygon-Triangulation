import matplotlib.pyplot as plt
import numpy as np

def createPolygon():    
    polygon = []
    lines = None
    
    def onclick(event):
        flag = True 
        ex, ey = event.xdata, event.ydata
        index = 0 

        for (x, y) in polygon:
            if abs(x - ex) < 3 and abs(y - ey) < 3:
                flag = False
                index = polygon.index( (x, y) )
        #

        if flag: 
            ax.plot([event.xdata], [event.ydata], marker='o', linestyle='-', color='b')

            if len(polygon) >=1: 
                ax.plot( [event.xdata, polygon[-1][0]], [event.ydata, polygon[-1][1]])
            #
            polygon.append( ( (event.xdata), (event.ydata) ) )
            fig.canvas.draw()
        
        else:
            ax.plot( [polygon[index][0], polygon[-1][0]], [polygon[index][1], polygon[-1][1]], marker='o', linestyle='-', color='b')
            fig.canvas.draw()

        #end 'if' clause
    #end procedure onclick()
    
    fig, ax = plt.subplots()
    ax.set_xlim((-20,20))
    ax.set_ylim((-20,20))
    ax.set_title("Draw points of a simple polygon in counter-clockwise order!")
    ax.axis('equal')
    
    cid = fig.canvas.mpl_connect('button_press_event', onclick)
    # plt.grid()

    plt.show()
    
    return polygon  
#end procedure drawPolygon()
