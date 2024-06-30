'''You are given two non-empty linked lists representing two non-negative integers. 
The most significant digit comes first and each of their nodes contains a single digit. 
Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

'''

'''1. Reverse the linked lists:
   - Reverse the order of nodes in both linked lists.
   - This step aligns the digits from the least significant to the most significant.
   - Reversing the lists allows for easier addition starting from the least significant digit.

2. Initialize the carry and sum:
   - Set the initial value of the carry to 0.
   - Create a dummy node to store the sum of the two numbers.
   - Initialize a pointer (e.g., `current`) to the dummy node.

3. Add the values of the nodes within a loop:
   - Traverse both reversed linked lists simultaneously.
   - For each iteration:
     - Get the values of the current nodes from both lists (if available, otherwise consider 0).
     - Add the values along with the carry.
     - Calculate the new carry and sum.
       - Carry = (value1 + value2 + previous_carry) // 10
       - Sum = (value1 + value2 + previous_carry) % 10
     - Create a new node with the sum as its value.
     - Append the new node to the result linked list.
     - Move the pointers to the next nodes in both lists.

4. Handle the remaining carry:
   - After the loop ends, check if there is any remaining carry.
   - If the carry is greater than 0, create a new node with the carry as its value.
   - Append the carry node to the result linked list.

5. Reverse the result linked list:
   - The result linked list currently represents the sum in reverse order.
   - Reverse the order of nodes in the result linked list.
   - This step ensures that the most significant digit is at the beginning of the linked list.

6. Return the result linked list:
   - The reversed result linked list represents the sum of the two numbers.
   - Return the head of the result linked list.'''

# Define a ListNode class to represent each node in the linked list
class ListNode:
    def __init__(self, val):
        self.val = val   # Store the value of the node
        self.next = None   # Initialize the next pointer to None

# Function to reverse a linked list
def reverse_list(head):
    prev = None   # Initialize the previous pointer to None
    current = head   # Set the current pointer to the head of the list
    
    # Traverse the linked list and reverse the pointers
    while current:
        next_node = current.next   # Store the next node
        current.next = prev   # Reverse the pointer of the current node to the previous node
        prev = current   # Move the previous pointer to the current node
        current = next_node   # Move the current pointer to the next node
    
    return prev   # Return the new head of the reversed list

# Function to add two numbers represented by linked lists
def add_two_numbers(l1, l2):
    # Reverse both linked lists to align the digits from least significant to most significant
    l1 = reverse_list(l1)
    l2 = reverse_list(l2)
    
    dummy = ListNode(0)   # Create a dummy node to simplify the addition process
    curr = dummy   # Set the current pointer to the dummy node
    carry = 0   # Initialize the carry to 0
    
    # Traverse both lists simultaneously until both lists are exhausted
    while l1 or l2:
        # Get the values of the current digits (or 0 if the list is exhausted)
        x = l1.val if l1 else 0
        y = l2.val if l2 else 0
        
        total = x + y + carry   # Calculate the sum of the digits and the carry
        carry = total // 10   # Update the carry for the next iteration
        curr.next = ListNode(total % 10)   # Create a new node with the digit value and append it to the result list
        curr = curr.next   # Move the current pointer to the newly created node
        
        # Move the pointers of both lists to the next node if they are not exhausted
        if l1:
            l1 = l1.next
        if l2:
            l2 = l2.next
    
    # If there is still a carry after the traversal, create a new node with the carry value
    if carry > 0:
        curr.next = ListNode(carry)
    
    # Reverse the resulting linked list to get the most significant digit at the beginning
    return reverse_list(dummy.next)

# Example usage
# Create the first linked list: 7 -> 2 -> 4 -> 3
node1 = ListNode(7)
node2 = ListNode(2)
node3 = ListNode(4)
node4 = ListNode(3)
node1.next = node2
node2.next = node3
node3.next = node4

# Create the second linked list: 5 -> 6 -> 4
nodea = ListNode(5)
nodeb = ListNode(6)
nodec = ListNode(4)
nodea.next = nodeb
nodeb.next = nodec

# Add the two numbers represented by the linked lists
result = add_two_numbers(node1, nodea)

# Print the resulting linked list
while result:
    print(result.val, end=" ")
    result = result.next