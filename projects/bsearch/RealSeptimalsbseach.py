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
      
# Hannah's new update 
def search(item,numbers):
        searchend=len(numbers)                                          # end of search
        search=0                                                                        # start of search
        found=False
        while(found==False):
                scope=(search+searchend)/2                              # scope to hold span of search
                if(item<numbers[scope]):
                        searchend=scope-1
                elif(item>numbers[scope]):
                        search=scope+1
                else:                                                                   # if its is not greater or less than it is equal to
                        found=True
                        return scope                                            # return correct index

      
      
#Hannah's bsearch

def search(item,numbers):
        searchend=len(numbers)                                          # end of search
        search=0                                                                        # start of search
        found=False
        while(found==False):
                scope=(search+searchend)/2                              # scope to hold span of search
                if(item<numbers[scope]):
                        searchend=scope-1
                elif(item>numbers[scope]):
                        search=scope+1
                else:                                                                   # if its is not greater or less than it is equal to
                        found=True
                        return scope                                            # return correct index


    
#Contee's search 


def  bsearch(item, list):

    low = 0

    up = len(list)-1
     
    
#setting the range to manipulate list for search. 

    while low <= up:
        
        
        mid= (low + up) / 2 #setting the midpoint
        
        if list[mid] < item:

            low = mid +1  #setting the new high midpoint

        elif list[mid] > item:

            up = mid - 1 #setting the new low midpoint

        elif list[mid] == item:

            
            return mid #returning the item 

        else:
            return -1


blist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]











