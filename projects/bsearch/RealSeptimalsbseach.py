# Alston Clark

def bsearch(list,search):




  top = len(list)

  bottom = 0

  
 

  if (top >= search >= bottom):
    return -1 

   
  while ( bottom != top):
    # when bottom == top then you have found the index

    mid = (top + bottom) / 2

    if (search < list[mid]):
      top = mid - 1


    elif ( search > list[mid]):
      bottom = mid + 1


    else:
      return mid


# Alston's Update

# Alston Clark

def bsearch(list,search):




  top = len(list)

  bottom = 0

  
 

  if (top < search) and (search < bottom):
    return -1 
  
  if (len(list) == 0):
    return -1 
    
   
  while ( bottom <= top):
    # when bottom == top then you have found the index



    mid = (top + bottom) / 2

    if (search < list[mid]):
      top = mid - 1


    elif ( search > list[mid]):
      bottom = mid + 1


    

    else:
      return mid


    














