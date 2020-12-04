# This code finds the number searched in using the algorithme called binary search

# We will check if the number looked for is bigger or smaller than middle value
# for ex. if value is smaller than middle value, 
# we will reduce our list ends with the number front of middle index 


def binary_search(serie, value):
    serie.sort()
    begin_indice = 0                                                            # We start from 0. index at the begining
    end_indice = len(serie)-1                                                   # And termine the interval with last element [here len(list)-1]

    while (end_indice >= begin_indice) and (len(serie) != 1):                                         # loops till there is one number 
        mid_indice = (end_indice + begin_indice) // 2            
        mid_point_value = serie[mid_indice]
        
        if mid_point_value == value:                                            # We termine the loop when we reach our goal
            return mid_indice

        elif mid_point_value < value:
            end_indice = mid_indice - 1
        else:
            begin_indice = mid_indice + 1
    
    return False

listem = [1,2,4,5,6,7,8]
aranan_eleman = 6

print(binary_search(listem,aranan_eleman))
# Always returns 'False' idk why
