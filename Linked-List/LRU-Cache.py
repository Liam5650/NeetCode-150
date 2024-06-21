class Node:

    def __init__(self, val):

        # We will use nodes in a linked list to handle the least-recently-used functionality. Nodes
        # at the head are the oldest, and nodes at the end are the latest. We use a prev pointer as well
        # to easily slice nodes from their position in the list
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):

        print("Initializing Cache. Capacity: " + str(capacity))

        # We need a hashtable that maps a key to a node so we can get to its position in O(1) time for changing priority
        self.nodes = {}

        # We need a separate hashtable to store the key-value pairs so they can be accessed in O(1) time
        self.pairs = {}

        # Reference pointers so we can access the start or end of the linked list in O(1) time
        self.head = None
        self.end = None

        # Keep track of the current usage
        self.size = 0
        self.capacity = capacity


    def get(self, key: int) -> int:
        
        print("Current keys: " + str(list(self.pairs)) + "\n" + "Fetching pair " + str(key))

        # If the key exists, return the pair and update the priority of the node since it was last accessed
        if key in self.pairs:
            print("Found pair for key " + str(key))
            node = self.nodes[key]
            self.updatePriority(node)
            return self.pairs[key]

        else:
            print("Pair not found")
            return -1


    def put(self, key: int, value: int) -> None:

        print("Current keys: " + str(list(self.pairs)))
        print("Processing pair " + str(key) + " : " + str(value))

        # First condition is to create the pair and linked list if no values have been added yet
        if self.size == 0:
            
            self.pairs.update({key : value})
            node = Node([key, value])
            self.nodes.update({key : node})
            self.head = node
            self.end = node
            self.size += 1
            print("Inserted pair")

        # Second condition is if there is still free capacity in the cache
        elif self.size < self.capacity:

            # If it is a new key:value pair, update the pairs and add a new node to the list
            if not key in self.pairs:
                self.pairs.update({key : value})
                node = Node([key, value])
                self.nodes.update({key : node})
                self.end.next = node
                node.prev = self.end
                self.end = node
                self.size += 1
                print("Inserted pair")

            # If it is an old pair, update the value and the priority of the node since it was last accessed
            else:
                node = self.nodes[key]
                node.val[1] = value
                self.pairs[key] = value
                self.updatePriority(node)

        # Third condition is if there is no capacity in the cache
        else:
            
            # If the key doesn't exist, remove the node at the head of the list
            if not key in self.pairs:
                print("Removing old pair")
                toRemove = self.head
                self.pairs.pop(toRemove.val[0])
                self.nodes.pop(toRemove.val[0])

                node = Node([key, value])
                self.nodes.update({key : node})
                self.pairs.update({key : value})

                # If the cache is greater than size 1, update positions
                if toRemove.next:
                    toRemove.next.prev = None
                    self.head = toRemove.next
                    self.end.next = node
                    node.prev = self.end
                    self.end = node
                
                # If the cache is less than size 1, initialize the list from the new node
                else:
                    self.head = node
                    self.end = node
                    node.next = None

                print("Old pair removed, new pair added")

            # If the key exists, update the value and position of the node
            else:
                node = self.nodes[key]
                node.val[1] = value
                self.pairs[key] = value
                self.updatePriority(node)


    def updatePriority(self, node):

        # If we are at the head and the cache size is bigger than 1, move to the end
        if node == self.head and node != self.end:
            node.next.prev = None
            self.head = node.next
            self.end.next = node
            node.prev = self.end
            node.next = None
            self.end = node

        # If we are somewhere else (implying larger than 1 cache), join the adjoining nodes and move to end
        elif node != self.end:
            node.prev.next = node.next
            node.next.prev = node.prev
            self.end.next  = node
            node.prev = self.end
            self.end = node

        # Otherwise, we are at the end and the node is already at max priority and nothing needs to be done
        
        print("Updated pair priority")