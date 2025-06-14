class HashTable:
    def __init__(self):
        self.table = {}


    @staticmethod
    def hash_function(value):
        return hash(value)


    def is_in_table(self, value):
        key = self.hash_function(value)
        if self.table.get(key) is not None:
            # If key is found, value is already in array
            return True
        else:
            return False


    def delete(self, key):
        '''Delete key from table, if it exists.'''
        if self.table.get(key):
            self.table.pop(key)
            return True
        else:
            return False


    def delete_value(self, value):
        '''Delete value from table, if it exists.
           Actually more complicated than deleting a key. The table
           must be searched for an entry equal to value. The first
           occurence found is deleted.
           
           Worst case complexity is O(n), as the whole table is linearly
           searched.
        '''
        for key in self.table.keys():
            if self.table[key] == value:
                return self.delete(key)
        
        # Value is not found
        return False


    def insert(self, value):
        key = self.hash_function(value)
        
        if self.table.get(key) is not None:
            self.collision(key, value)
            return True
        else:
            self.table[key] = value
            return False
    

    def collision(self, key, value):
        # Open Addressing with Linear probing
        # Worst time complexity O(n), n is the size of hash table
        index = 0
        while self.table.get(key+index):
            # Iterate keys until an empty slot is found
            index += 1
        
        self.table[key+index] = value
