class NodeLinkedList:
    '''
        Node of a doubly linked list 
    '''
    def __init__(self, next = None, 
                    prev = None, data = None): 
        self.next = next # reference to next node in DLL 
        self.prev = prev # reference to previous node in DLL 
        self.data = data 

# Function to insert a node at the 
# beginning of the Doubly Linked List 
def push(head, new_data): 

    new_node = NodeLinkedList(data = new_data) 

    new_node.next = head 
    new_node.prev = None

    if head is not None: 
        head.prev = new_node 

    head = new_node 
    return head 

# Utility function to find the size of 
# Doubly Linked List 
def size(head): 
    last_node = head 
    list_size = 0
    while True: 
        list_size+= 1
        if last_node.next != None:
            last_node = last_node.next
        else:
            break
    return list_size, last_node

# Function to print linked list 
def printList(head): 

    node = head 

    while(node is not None): 
        print(node.data, end = " "), 
        last = node 
        node = node.next

# Rotate by modifying values
# Not the most efficient way
def rotate(head):
    current_node = head
    temp_odd  = None
    temp_even = None
    while True:
        if current_node == head:
            temp_odd = current_node.data
        elif temp_even == None:
            temp_even = current_node.data
            current_node.data = temp_odd
            temp_odd  = None
        elif temp_odd == None:
            temp_odd = current_node.data
            current_node.data = temp_even
            temp_even = None
        
        if current_node.next == None:
            break
        else:
            current_node = current_node.next
            
    if temp_even == None:
        head.data = temp_odd
    else:
        head.data = temp_even
        
    return head

# Rotate N steps by changing pointers
def rotate(head, steps):
    list_len, last_node = size(head) # Complexity O(n)
    steps    = steps % list_len

    # Clockwise rotation of list by N steps is equivalent to
    # counter-clockwise rotation of Head by N steps
    
    new_head_index = list_len - steps # List is zero-indexed
    
    # Get element at position N
    # N steps when N == list_len
    index = 0
    new_head = head
    while index != new_head_index:
        new_head = new_head.next
        index += 1

    # Actual rotation
    last_node.next = head
    head.prev  = last_node
    
    new_head.prev.next = None
    new_head.prev = None
    
    
    return new_head
    
# Test Code 
if __name__ == "__main__": 
    head = None

    head = push(head, 'e') 
    head = push(head, 'd') 
    head = push(head, 'c') 
    head = push(head, 'b') 
    head = push(head, 'a') 

    print("Initial list")
    printList(head) 
    print("\n") 
    
    N = 6

    head = rotate(head, N)

    print(f"Rotate list by {N} steps")
    printList(head)
