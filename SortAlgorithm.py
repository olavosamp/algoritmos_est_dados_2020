class SortAlgorithm:
    def __init__(self):
        self.steps = 0


    @staticmethod
    def swap(array, index_one, index_two):
        '''Swap values array[index_one] and array[index_two]
        '''
        temp = array[index_one]
        array[index_one] = array[index_two]
        array[index_two] = temp
        return array

    def sort(self, array):
        raise NotImplementedError
