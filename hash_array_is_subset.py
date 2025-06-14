# Find whether array2 is subset of array 1
# Assume both arrays are unordered and that there are not duplicated
# elements in each array.
import sys
from HashTable import HashTable

def is_subset_two_loops(base, subset):
    # Iterate both arrays
    # Complexity O(n*m)
    for i in range(len(subset)):
        found = False
        for j in range(len(base)):
            if subset[i] == base[j]:
                found = True
        if not(found):
            return False
    return True


def is_subset_hash(base, subset):
    # Time complexity:
    # O(n + m*a), a = number_elements/number_keys
    hash_table = HashTable()

    for i in range(len(base)):
        hash_table.insert(base[i])
    
    # print(hash_table.table)
    for j in range(len(subset)):
        if not hash_table.is_in_table(subset[j]):
            # If any element of subset candidate array is not found in base
            # array, it is not a subset
            return False
    
    # If this point is reached, all elements of subset array have been found
    # in base array.
    return True


if __name__ == "__main__":
    array1 = [1, 4, 5, 33, 65, 9, 0, 12, 4]
    array2 = [4, 12, 9, 1]

    print("array1: ", array1)
    print("array2: ", array2)

    print("\nIs array2 subset of array1?")

    print("Two loops")
    print(is_subset_two_loops(array1, array2))

    print("Hash table")
    print(is_subset_hash(array1, array2))

    # # Hashtable test
    # hash_table = HashTable()
    
    # print(hash_table.table)
    # hash_table.insert("zazo")
    
    # print(hash_table.table)
    # hash_table.insert("bb")
    
    # print(hash_table.table)
    # hash_table.insert("ozymandios")
    
    # print(hash_table.table)
    # hash_table.insert("zazo")

    # print(hash_table.table)
    # print(sys.getsizeof(hash_table.table), "bytes")
