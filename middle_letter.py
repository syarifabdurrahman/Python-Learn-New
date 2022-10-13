def mid(anything):
    
    if len(anything)%2 == 0:
        return ""
    else:
        allString= int(len(anything)/2)
        return anything[allString: allString+1]
       
            
mid("AABAA")