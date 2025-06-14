# TODO: Get problem and solve

import sys
from HashTable import HashTable

class NodeLinkedList:
    '''
        Node of a doubly linked list 
    '''
    def __init__(self, next = None, 
                    prev = None, data = None): 
        self.next = next # reference to next node in DLL 
        self.prev = prev # reference to previous node in DLL 
        self.data = data 


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
