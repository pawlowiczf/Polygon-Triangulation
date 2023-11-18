class Node():
    #
    def __init__(self, color, next = None):
        self.color = color 
        self.next  = None 
    #
#end class Node()
        
def createLinkedList(colors):
    #
    array = [ Node(color) for color in colors]

    for idx in range( len(array) ):
        #
        pointer = array[idx]
        pointer.next = array[ ( idx + 1 ) % len(array) ]
    #
        
    return array[0]
#end procedure createLinkedList()
