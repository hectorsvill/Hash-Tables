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
        if self.storage[index] is None:
            # add to respective bucket
            self.storage[index] = linkPair
        else:

            head = self.storage[index]
            
            if head.next is None:
                pass
            else:   
                while head:
                    head = head.next

            head.next = linkPair


    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''
        pass


    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''

        for key in self.storage: 
            if key == key.key:
                return key 

        pass


    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        pass


    ## helpers 

    def printBucketKeys(self):
        for bucket in self.storage:
            if bucket == None:
                print("Empty-bucket", end="")
            else:
                head = bucket
                while head:
                    print(head.key, end=" ")
                    head = head.next
            
            print("")


if __name__ == "__main__":
    
    # hashtable only has 3 buckets
    ht = HashTable(3)

    ht.insert("key-0","this is a zero")
    ht.insert("key-1", "Tiny hash table")
    ht.insert("key-2", "Filled beyond capacity")
    # ht.insert("key-3", "Linked list saves the day!")

    ht.printBucketKeys()
    # print("")

    # # Test storing beyond capacity
    # print(ht.retrieve("line_1"))
    # print(ht.retrieve("line_2"))
    # print(ht.retrieve("line_3"))

    # # Test resizing
    # old_capacity = len(ht.storage)
    # ht.resize()
    # new_capacity = len(ht.storage)

    # print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # # Test if data intact after resizing
    # print(ht.retrieve("line_1"))
    # print(ht.retrieve("line_2"))
    # print(ht.retrieve("line_3"))




