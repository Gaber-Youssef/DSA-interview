"""
Quick summary: 
    unordered collection that maps keys to values using hashing.
Also known as: 
    hash, hash map, map, unordered map, dictionary, associative array.
Important facts:
    - Stores data as key-value pairs.
    - Can be seen as an evolution of arrays that removes the limitation of sequential numerical 
      indices and allows using flexible keys instead.
    - For any given non-numeric key, hashing helps get a numeric index to look up in the 
      underlying array.
    - If hashing two or more keys returns the same value, this is called a hash collision. 
      To mitigate this, instead of storing actual values, the underlying array may hold 
      references to linked lists that, in turn, contain all values with the same hash.
    - A set is a variation of a hash table that stores keys but not values.
Pros:
    - Keys can be of many data types. The only requirement is that these data types are hashable.
    - Average search, insertion and deletion are O(1).
Cons:
    - Worst-case lookups are O(n).
    - No ordering means looking up minimum and maximum values is expensive.
    - Looking up the value for a given key can be done in constant time, but looking up the keys for a given value is O(n).
Notable uses:
    - Caching.
    - Database partitioning.
Time complexity (worst case):
    - Access: O(n)
    - Search: O(n)
    - Insertion: O(n)
    - Deletion: O(n)
"""

class HashMap:
    def __init__(self):
        self.size = 10
        self.map = [None] * self.size
        
    def _get_hash(self, key):
        """
        The function calculates the hash value of a given key by summing the ASCII values of its
        characters and returning the remainder when divided by the size of the hash table.
        
        :param key: The key parameter is the value that we want to hash. It can be any data type that
        can be converted to a string, such as a string, integer, or float
        :return: The code is returning the hash value of the given key.
        """
        hash = 0
        for char in str(key):
            hash += ord(char)
        return hash % self.size
    
    def add(self, key, value):
        """
        The function adds a key-value pair to the hash table. It first calculates the hash value of the
        key, then creates a list at that index in the hash table if one does not exist. It then appends
        the key-value pair to the list.
        
        :param key: The key parameter is the key of the key-value pair to be added to the hash table.
        :param value: The value parameter is the value of the key-value pair to be added to the hash table.
        :return: The function does not return anything.
        """
        key_hash = self._get_hash(key)
        key_value = [key, value]
        
        if self.map[key_hash] is None: # if the key does not exist in the hash table
            self.map[key_hash] = list([key_value])
            return True
        else: # if the key already exists in the hash table
            for pair in self.map[key_hash]:
                if pair[0] == key:
                    pair[1] = value
                    return True
            self.map[key_hash].append(key_value)
            return True
        
    def get(self, key):
        """
        The function returns the value of a given key from the hash table. It first calculates the
        hash value of the key, then iterates through the list at that index in the hash table until
        it finds the key-value pair with the matching key. It then returns the value from that pair.
        
        :param key: The key parameter is the key of the key-value pair to be retrieved from the hash table.
        :return: The function returns the value of the key-value pair with the given key.
        """
        key_hash = self._get_hash(key)
        if self.map[key_hash] is not None:
            for pair in self.map[key_hash]:
                if pair[0] == key:
                    return pair[1]
        return None
    
    def delete(self, key):
        """
        The function deletes a key-value pair from the hash table. It first calculates the hash value
        of the key, then iterates through the list at that index in the hash table until it finds the
        key-value pair with the matching key. It then removes the pair from the list.
        
        :param key: The key parameter is the key of the key-value pair to be deleted from the hash table.
        :return: The function does not return anything.
        """
        key_hash = self._get_hash(key)
        
        if self.map[key_hash] is None:
            return False
        for i in range(0, len(self.map[key_hash])):
            if self.map[key_hash][i][0] == key:
                self.map[key_hash].pop(i)
                return True
            
    def print(self):
        """
        The function prints all the key-value pairs in the hash table.
        
        :return: The function does not return anything.
        """
        for item in self.map:
            if item is not None:
                print(str(item))
                
    def keys(self):
        """
        The function returns a list of all the keys in the hash table.
        
        :return: The function returns a list of all the keys in the hash table.
        """
        keys = []
        for item in self.map:
            if item is not None:
                # print(item)
                for pair in item:
                    keys.append(pair[0])
        return keys
    
    def values(self):
        """
        The function returns a list of all the values in the hash table.
        
        :return: The function returns a list of all the values in the hash table.
        """
        values = []
        for item in self.map:
            if item is not None:
                for pair in item:
                    values.append(pair[1])
        return values
    
if __name__ == "__main__":
    h = HashMap()
    h.add('Bob', '567-8888')
    h.add('Ming', '293-6753')
    h.add('Ming', '333-8233')
    h.add('Ankit', '293-8625')
    h.add('Aditya', '852-6551')
    h.add('Alicia', '632-4123')
    h.add('Mike', '567-2188')
    h.add('Aditya', '777-8888')
    h.print()
    h.delete('Bob')
    h.print()
    print('Ming: ' + h.get('Ming'))
    print(h.keys())
    print(h.values())