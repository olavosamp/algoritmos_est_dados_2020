from SortAlgorithm import SortAlgorithm
from QuickSort import QuickSort

class MergeSort:
    def __init__(self):
        pass

    def sort(self, array):
        pass
        

class InsertionSort(SortAlgorithm):
    # def __init__(self):
    # pass

    def sort(self, array):
        for i in range(1, len(array)):
            j = i
            while j > 0 and array[j-1] > array[j]:
                self.swap(array, j-1, j)
                j -= 1
        return array

if __name__ == "__main__":
    array_to_order = [99, 0, 8, 5, 4, 10, 3, 22, 6]
# [0, 5, 8, 99, 4, 10, 3, 22, 6]
    print("Unordered array:\n", array_to_order)

    print("Sorting...")
    # sort_algo = QuickSort()
    # ordered_array = sort_algo.quicksort(array_to_order, 0, len(array_to_order)-1)
    # print("\nOrdered array w/ quicksort")
    # print(ordered_array)
    
    sort_algo = InsertionSort()
    ordered_array = sort_algo.sort(array_to_order)
    print("\nOrdered array w/ insertion sort")
    print(ordered_array)
