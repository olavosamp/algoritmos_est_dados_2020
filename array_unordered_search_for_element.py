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

if __name__ == "__main__":
    array = [3, 4, 2, 10, 6, 5, 8]
    
    target = 99
    
    print("Array:\n", array)
    print("Target element:", target)
    print("\nSearching...")
    target_index = search_unordered(array, target)
    if target_index is not None:
        print("\nFound element at index: ", target_index)
    else:
        print("\nElement not found.")