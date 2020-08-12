"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next

    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev        
"""
Our doubly-linked list class. It holds references to 
the list's head and tail nodes.
"""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length
    
    """
    Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly.
    """
    def add_to_head(self, value):
        #create a new_node
        new_node = ListNode(value, None, None)
        #check if dll is empty, if so then head  and tail refer to new node
        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node 
            self.head = new_node
            self.length += 1
        
    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):
        val = self.head.value
        # remove head+1's prev to Null (do we have to set the head's next to null? )
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.head.next.prev = None
            # point head to head +1
            self.head = self.head.next

        self.length -= 1
        return val
            
    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
            # create new node. # node prev to head. node next is null
        node = ListNode(value)
        if self.head is None or self.tail is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            # node head next to new node
            self.tail = node
        self.length += 1
            
    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        val = self.tail.value
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            # tail's previous node's next: set to null (do we set tail's prev to nulL?)
            self.tail.prev.next = None
            # point tail to tail's previous node
            self.tail = self.tail.prev
            
        self.length -= 1
        
        return val
            
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        #remove node set prev to next
        node = self.head 
        sec_last = None # To maintain the track of 
                        # the second last node 
  
    # To check whether we have not received  
    # the empty list or list with a single node 
        if not node or not node.next:  
            return
  
        # Iterate till the end to get 
        # the last and second last node  
        while node and node.next : 
            sec_last = node 
            node = node.next
  
        # point the next of the second 
        # last node to None 
        sec_last.next = None
  
        # Make the last node as the first Node 
        node.next = self.head 
        self.head = node 
       
        
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        found = False
        current_node = self.head
        while found == False:
            if current_node == node:
                found = True        
                if current_node != self.tail:
                    if current_node == self.head: # if current node is head
                        current_node.next.prev = None
                        self.head = current_node.next
                    else: 
                        current_node.next.prev = current_node.prev
                        current_node.prev.next = current_node.next
                    current_node.prev = self.tail
                    self.tail.next = current_node
                    self.tail = current_node
            else:
                found = False
                current_node = current_node.next

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):
        #is there anything to delete
        if self.head is None and self.tail is None:
            return None
        #check if there is only one node
        if node is self.head and node is self.tail:
            self.head = None
            self.tail = None
        #check if node is the head or tail
        #otherwise the node is some node in the middle
        elif node is self.head:
            self.head = node.next
            node.delete()
        elif node is self.tail:
            self.tail = node.prev
            node.delete()
        else:
            node.delete()
            #don't forget to decrement the length
        self.length -= 1

    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self):
        #if list is empty return None
        if self.head is None and self.tail is None:
            return
        #keep track of the current node
        max_value = self.head.value
        #traverse the entirety of the linked list
        current=self.head.next

        while current is not None:
        #if we see a value > the largest value we've seen so far
            if current.value > max_value:
             #update the largest value
                max_value = current.value
            #update current to point to the next node
                current = current.next
             #return largest value
        return max_value 
       
       
        

    