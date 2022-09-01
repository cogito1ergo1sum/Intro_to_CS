def find_subset_recursive(initial_set, current, index, subsets):
    #use 'index' to point to which element in the initial set must be processed.
    #We must consider all options where each element is either included in the subset or it is not.

    # Base Case: if no more elements in initial set to process, save the the current subset
    if index < 0:
        return subsets.append( list(current) )

    # Option 1: current element is included in the subset
    current.append( initial_set[index] )
    find_subset_recursive(initial_set, current, index - 1, subsets)

    # Option 2: current element is NOT included in the subset
    current.pop()
    find_subset_recursive(initial_set, current, index - 1, subsets)


# Program to generate all distinct subsets of given set
def get_all_subsets(initial_set):
    current = [] #aux list to store current subset
    subsets = [] #output list with all subsets
    find_subset_recursive(initial_set, current, len(initial_set) - 1, subsets)
    return subsets


print('With set [], subsets are:', get_all_subsets( [] ) ) #expected result: []
print('With set [1], subsets are:', get_all_subsets( [1] ) ) #expected result: [], [1]
print('With set [1,2], subsets are:',get_all_subsets([1, 2]))  # expected result: [], [1], [2], [1,2]
print('With set [1,2,3], subsets are:', get_all_subsets( [1,2,3] ) ) #expected result: [], [1], [2], [3], [1,2],[1,3], [2,3], [1,2,3]

'''
Time complexity analysis
O(2^n)
We are implicitly iterating over the initial list [ O(n) ].
And for each iteration we consider all elements to be included or not O(2^n)
So time complexity is: O(n)*O(2^n) = O(n * 2^n)
'''
