''' Group 5 Members:

Hannah M. Clark
Lena Alston
Cesa Salaam
Sarah Jones
Jabari Olatunji 
Contee Cameron 
Courtney Gaines
Attiyah Laneir
Alston Clark
'''
''' Helpers:
Barry Harris
'''




# Alston Clark

def bsearch(list,search):




  top = len(list)

  bottom = 0

  
 

  if (top < search) and (search < bottom):
    return -1 
  
  if (len(list) == 0):
    return -1 
    
   
  while ( bottom <= top):
  



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


    
#Lena's bsearch 
def bsearch(list, element):              #bsearch function definition 
    if len(list) != 0:                     #condition checking for emptiness 
        first = 0                   
        last = len(list)-1                #declaration of last index variable 
        found = False                        #bool found variable defined 
        while not found:                  #while loops until element is found 
            midpoint = (first + last)/2         #updates midpoint checking
            if (first==last) and (element != list[first]):      #when one element is left to be searched and that element is not the desired value   
                print 'Element is not in list.'     
                return -1                                   #ends function 
            elif element < list[midpoint]:              #if element is less than element at current list position 
                last = midpoint - 1                     #updates last index value 
            elif element > list[midpoint]:              #if element is greater than element at current list positon 
                first = midpoint + 1                    #updates first index value 
            else:                                       #else element equals element at current list positon 
                found = True                        #ends while loop 
                return midpoint     #returns index of searched element 
    else:                           #list is empty 
        print 'Element cannot be found. List is empty.'
        return -1


#Attiyah's bsearch
#bsearch: binary search function of sorted list 
def bsearch (searchList, element):
    first = 0 #variable used to manuvear through list
    last = len(searchList) - 1    #variable used to manuvar through list
    midPoint = (first + last) / 2       #variable used to split list in half
    found = False    #variable to mark whether the element has been found in the list 
    
    #print "My first element is ", searchList[first]
    #print "My last element is ", searchList[last]
    #print "My midpoint is ", searchList[midPoint]

    while found == False and first <= last:    #while loop used to look through entire list once
        
        if element > searchList[midPoint]:      #conditional used to determine whether to search the upper or lower half of the list
            first = midPoint + 1                #changes the first position to the midpoint + 1
            midPoint = (first + last) /2        #updates the midpoint 
            found = False                       #updates the value of found

        elif element < searchList[midPoint]:    #used to determine whether to search the lower or upper half of the list
            last = midPoint - 1                 #changed the last poistion to midpoint - 1
            midPoint = (first + last) / 2       #updates the midpoint
            found = False                       #updates the value of found

        elif element == searchList[midPoint]:   #if the element is found
            found = True                        #found is set to True, exiting the loop

    if found == False:                          #if statement to return false if element is not found
        return -1

    
    return midPoint                             #if statement to return the index of the element if found

#myList = [22,33,44,55,66,77,88,99]              #declaration and assignment of myList 
#print bsearch(myList,9)                         #function call to bsearch passing the variable myList

#Cesa Salaam.
def bsearch (List, element):
    bottom = 0
    top = len(List)-1
    if len(List)== 0:
        return -1
    elif len(List)!= 0:
        if element <= List[top] and element >= List[0]:
            
                while top >= bottom:
                    middle = (bottom+top)//2
                    if element == List[middle]:
                        return middle
                    elif element > List[middle]:
                        bottom = middle + 1
                    elif element < List[middle]:
                        top = middle - 1
        else:
            return -1

#Sarah Jones
def bsearch( lista, element):
    start = 0
    end = len(lista) - 1
    while (end >= start):
          mid = (start + end) / 2
          if (lista[mid] < element):
            start = mid + 1
          elif lista[mid] > element:
            end = mid - 1
          else:
            return mid
            
        
    return -1
    
#Contee Cameron

def  bsearch(ist, item):

    low = 0

    up = len(ist)-1
    

    while low <= up:
            
        mid= (low + up) / 2
        
        
        if ist[mid] < item:

            low = mid +1
            

        elif ist[mid] > item:

            up = mid - 1
            

        elif ist[mid] == item: 
    
            return mid
        
        elif len(ist) == 0:

            return -1

        else:
            return -1

# Hannah M. Clark 

def search(item,numbers):

	if(len(numbers)==0):
		return -1 
	searchend=len(numbers)					
	search=0							
	found=False
	notthere=False
	while(found==False and search<searchend):
		scope=(search+searchend)/2 			
		if(item<numbers[scope]):
			searchend=scope-1
		elif(item>numbers[scope]):
			search=scope+1
		else:									
			found=True
			return scope 
	return -1





#Courtneys Code

def bsearch(listt,e):


    start = 0

    end = len(listt)-1

    mid = (start + end) /2 #needed to define your mid point not e


    while (e != mid and start<end): 

        if e < listt[mid]: #if the element being searched for is less than your midpoint

            end = mid-1

            mid = (start + end)/2

        elif e> listt[mid]: #if element being searched for is greater than your midpoint
            start = mid + 1
            mid = (start + end) /2

        else:

            return mid #index of found element is held by mid

    return -1   #element was not found 



#Attiyah's bsearch
def bsearch(searchList, element):
    first = 0
    last = len(searchList) - 1
    midPoint = (first + last) / 2
    found = False
    
    

    while found == False and first <= last:
        
        if element > searchList[midPoint]:
            first = midPoint + 1
            midPoint = (first + last) /2
            found = False

        elif element < searchList[midPoint]:
            last = midPoint - 1
            midPoint = (first + last) / 2
            found = False

        elif element == searchList[midPoint]:
            found = True

    if found == False:
        return -1
    
# Jabari's Code
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
