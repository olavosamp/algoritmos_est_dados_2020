from SortAlgorithm import SortAlgorithm

class QuickSort(SortAlgorithm):
    def __init__(self):
        pass


    def partition(self, array, left, right):
        pivot = self.array[int((left+right)/2)] # Pick middle element

        while left <= right:
            while array[left] < pivot:
                left += 1
            
            while array[right] > pivot:
                right -= 1
            
            # Swap left and right elements
            if left <= right:
                self.array = self.swap(self.array, left, right)
                left  += 1
                right -=1
        return left


    def quicksort(self, array, left, right):
        self.array = array
        index = self.partition(self.array, left, right)

        if left < index-1:
            self.array = self.quicksort(self.array, left, index-1)
        
        if index < right:
            self.array = self.quicksort(self.array, index, right)

        return self.array
