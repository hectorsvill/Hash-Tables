# '''
# Linked List hash table key/value pair
# '''
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

    def insert(self, key, value):
        l = LinkedPair(key, value)
        if self.next is None:
            self.next = l
        else:
            head = self.next
            while head:
                head = head.next
            head = l


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
            # print("bucket is not empty  ")
            #(self.storage[index]).insert(key,value)
            head = self.storage[index]
            # print(head)
            while head.next is not None:
                if head.key == key:
                    head.value = value
                    return
                head = head.next
            head.next = linkPair



    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''
        # reconect link list

        pass


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
            if head.key == key:
                return head.value
            while head:
                if head.key == key:
                    return head.value
                head = head.next

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
                print("🗑", end="")
            else:
                head = bucket
                while head:
                    print(head.key, end=" ")
                    head = head.next
            
            print("")


if __name__ == "__main__": 
    
    # hashtable only has 3 buckets

    ht = HashTable(2)
    ht.insert("key-0", "val-0")
    ht.insert("key-1", "val-1")
    ht.insert("key-2", "val-2")
    ht.insert("key-3", "val-3")
    ht.insert("key-4", "val-4")
    ht.insert("key-5", "val-5")
    ht.insert("key-6", "val-6")
    ht.insert("key-7", "val-7")
    ht.insert("key-8", "val-8")
    ht.insert("key-9", "val-9")

    ht.printBucketKeys()
    print("")
    ht.insert("key-9", "new val-9")
    print(ht.retrieve("key-9"))
    
    
    print("")
    ht.insert("key-9", "new val-9")
    print(ht.retrieve("key-9"))
    ht.printBucketKeys()