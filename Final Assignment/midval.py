def unimodal_sort(array):
    # assigned start and end comparison values to 0 and -1
    # since the list is increasing and then decreasing (unimodal),
    # it makes sense to compare outside-in as the original array is 2 conjoined sorted lists (increasing+decreasing)
    # result list starts as empty list before values are sorted into it

    start = 0
    end = -1
    result = []
    #while loop assures loop doesn't continue when array list is empty
    while len(array) >= 1:
            # if the value of the first element is less than/equal to the last element, remove 1st element from array and add it to result list
            if array[start] <= array[end]:
                result.append(array.pop(start))
            #otherwise vice versa because last element is the lesser value
            else:
                result.append(array.pop(end))
    #return sorted array (min to max)
    return result


####################### end of code###########################

###tests####
a = [5, 9, 20, 70, 6, 5, 4, 2, -1]
sort = unimodal_sort(a)
print(sort)
b = [-4, 9, 25, 14, 6, -4]
sort = unimodal_sort(b)
print(sort)
c = [0, 3, 5, 2, 0]
sort = unimodal_sort(c)
print(sort)
d = [0, 1, 0]
sort = unimodal_sort(d)
print(sort)
e = [2, 12000, -1]
sort = unimodal_sort(e)
print(sort)

'''
First 3 lines of the function are assigment operations, O(3).
The while loop: (O)n as while loop will not terminate until 0 elements are left in the array.
    So this while loop scales the entire array, giving us n, the length of the array.
If statement: O(3): 2 array index operations and 1 logical operation <=
result.appen line: O(2): 2 operations:pop and append (which do not need to iterate over the entire list like remove and extend
    would since these methods know the location of the element (here we use start: array[0], the first element in the array)
Else statement: O(2): 2 operations, similar logic to above as we are using append and pop and know the locations of the elements in these methods
Return statment: O(1) operation for return statement
Overall: Ignoring constants, we would have O(n).

Time complexity is a O(n) as we need to iterate over all elements in the array 
at least once in order to compare which is smaller value and add in increasing 
order to result list. 
This is dependent of the length of the list, so the execution time of this 
algorithm is dependent on the length of the array. 
'''
