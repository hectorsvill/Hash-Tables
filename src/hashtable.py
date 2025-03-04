# '''
# Linked List hash table key/value pair
# '''
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''
    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity
    # check _hash_mod
    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        return hash(key)
    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash

        OPTIONAL STRETCH: Research and implement DJB2
        '''
        pass

        #look at _hash
    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash(key) % self.capacity
    def insert(self, key, value):
        '''
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Fill this in.
        '''
        # create index with hash_mod
        index = self._hash_mod(key)
        #create link pair 
        linkPair = LinkedPair(key, value)
        # check if hashtable is empty
        if self.storage[index] == None:
            # add to respective bucket
            self.storage[index] = linkPair
        else:
            head = self.storage[index]
            while head.next is not None:
                if head.key == key:
                    head.value = value
                    return
                else:
                    head = head.next
            if head.key == key:
                head.value = value
            else:
                head.next = linkPair
    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''
        # reconect link list
        index = self._hash_mod(key)
        storage = self.storage[index]
        if storage.next is None:
            self.storage[index] = None
        else:
            # stoer current and previous 
            head = storage
            prev = None
            while head is not None:
                if head.key == key:
                    break
                prev = head
                head = head.next
            prev.next = head.next
    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
        #find index
        index = self._hash_mod(key)
        # print(index)
        storage = self.storage[index]
        if storage is None:
            return None
        else:
            head = storage
            while head is not None:
                if head.key == key:
                    return head.value
                else:
                    head = head.next
    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        old_storage  = self.storage
        self.capacity *= 2
        self.storage = [None] * self.capacity
        
        for bucket in old_storage:
            if bucket == None:
                pass
            else:
                head = bucket
                while head:
                    self.insert(head.key, head.value)
                    head = head.next




    # helpers 
    def printBucketKeys(self):
        for bucket in self.storage:
            if bucket == None:
                print("[]")
            else:
                head = bucket
                while head:
                    print(head.key, end=" ")
                    head = head.next
            print("")


if __name__ == "__main__": 
    ht = HashTable(2)    
    
    
    ht.insert("key-0", "val-0")
    ht.insert("key-1", "val-1")
    ht.insert("key-2", "val-2")
    ht.insert("key-3", "val-3")
    ht.insert("key-4", "val-4")
    ht.insert("key-5", "val-5")
    
    ht.resize()

    ht.printBucketKeys()
    # ht.remove("key-2")
    # ht.printBucketKeys()