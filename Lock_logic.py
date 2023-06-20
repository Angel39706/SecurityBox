import time
from Lock import Open, Close
#from Hall import HL
import time


def LockL():
    OC = True
    if(OC == True):
        Open()
        #Opening()
        OC = False
        time.sleep(30)
        OC = True
        if(OC == True):
            Close()
    
            
        
    
