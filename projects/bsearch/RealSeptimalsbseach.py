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
      
   # JabariOLatunjibsearch   
      def bsearch(list,item):
    
      top =  len(list)-1
      
      bottom = 0
      
      found = False
      
      while found == False:
          
          search = (top+bottom)/2
          
          if item > list[search]:
              
             bottom = search + 1
             
        
          elif item < list[search]:
              
              top = search -1
          if item not in list:
              return -1  
            
              
          elif item == list[search]:
    
              return search


    












