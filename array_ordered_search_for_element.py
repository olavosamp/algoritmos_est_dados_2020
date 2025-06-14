# Search for an element in an unordered array

def search_unordered(array, target):
    index = 0
    array_len = len(array) # O(1) if array stores memory range
    while index < array_len:
        if array[index] == target:
            return index
        else:
            index += 1
    return None
    
def search_ordered(array, target):
    # Using binary search

    answer_index = int(len(array)/2)
    while True:
        array_len = len(array)
        pivot_index = int(array_len/2)
        test_element = array[pivot_index]
        
        print("pivot:", pivot_index)
        print("test_elem:", test_element)
        if test_element == target:
            return answer_index
        elif target < test_element:
            new_start = 0
            new_end   = pivot_index-1
        elif target > test_element:
            new_start = pivot_index+1
            new_end   = array_len-1     # new_end is decreased by one to be able
                                        # to reach zero and used as stopping cond
        
        print("new_start ",new_start)
        print("new_end ",new_end+1)
        if new_start == new_end+1:
            return -1
        
        array = array[new_start:new_end+1]
        answer_index = pivot_index+len(array)
        print("new array\n", array)
        #input()

if __name__ == "__main__":
    array = [2, 4, 5, 6, 10, 15, 80]
    
    target = 15
    
    print("Array:\n", array)
    print("Target element:", target)
    print("\nSearching...")
    target_index = search_ordered(array, target)
    if target_index != -1:
        print("\nFound element at index: ", target_index)
    else:
        print("\nElement not found.")