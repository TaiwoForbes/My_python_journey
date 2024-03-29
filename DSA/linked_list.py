class Node:
    """  
    Node
    """
    data = None
    next_node = None

    def __init__(self,data):
        self.data = data

    def __repr__(self):
        """  
        String representation of data in our node
        """
        return f"<Node data: {self.data}>"

class LinkedList:
    
    def __init__(self):
        self.head = None

    def add(self,data):
        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node

    def search(self,key):
        """  
        Search for the first node containing data that matches the key
        Return the node or None if not found

        Takes 0(n) time
        """
        current = self.head
        while current:
            if current.data == key:
                return current
            else:
                current = current.next_node


    def insert(self,data,index):
        """ 
        Insert a new node containing data at index position .
        Insertion takes O(1) time ut finding the node at the insertion point takes O(n)
        
        Takes overall O(n) time
        """

        if index == 0:
            self.add(data)

        elif index > 0:
            new =  Node(data)
            position = index
            current = self.head

            while position > 1:
                current = current.next_node
                position -= 1
            prev_node = current
            next_node = current.next_node

            prev_node.next_node = new
            new.next_node = next_node
    
    def remove(self,key):
        """  
        Remove Node containing data that matches the key
        Returns the node or None if key doesn't exist
        Takes O(n) time
        """
        current = self.head
        previous = None
        found = False

        while current and not found:
            if current.data == key and current is self.head:
                found = True
                self.head = current.next_node
            elif current.data == key:
                found = True
                previous.next_node = current.next_node
            else:
                previous = current
                current = current.next_node
        return current

    def size(self):
        count = 0
        current = self.head
        while(current):
            count+= 1
            current = current.next_node
        return count


    def node_at_index(self,index):
        if index == 0:
            return self.head
        else:
            current = self.head
            position = 0

            while position < index:
                current = current.next_node
                position += 1

            return current

    def __repr__(self):
        """  
        String representation of node
        """
        nodes = []
        current = self.head

        while(current):
            if current is self.head:
                nodes.append(f"[HEAD: {current.data}]")
            elif current.next_node is None:
                nodes.append(f"[TAIL: {current.data}]")
            else:
                nodes.append(f"[{current.data}]")
                

            
            current = current.next_node
        return "-> ".join(nodes)


if __name__ == "__main__": 
    N1 = Node(20)
    N2 = Node(10)
    N1.next_node = N2

    print(N1.data) # Linked List of add is same thing as demonstrated above. We need to instantiate new object
    l = LinkedList()
    l.add(2)
    l.add(4)
    l.add(6)
    print(l.size())

    print(l.search(2))
    print(l)
    l.insert(7,2)
    l.insert(8,2)
    print(l)
    print(l.size())

    print(l.remove(4))
    print(l.size())
    print(l)
