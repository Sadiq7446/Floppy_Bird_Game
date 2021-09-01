""" Python script to create a doubly linked list for the following operations
   - Insert a Node at Beginning, at Ending and at a given Position
   - Delete a Node at Beginning, at Ending and at a given Position
   - Search, Count the Number of Nodes and Display """

# Write your code from here

# Created a Node class to insert a node in linkedlist
class Node:
    def __init__(self, data, next, prev):
        self.data = data
        self.next = next
        self.prev = prev


# Created a Doubly Linked List class
class DoublyLinkedList:
    # A head function for linked lists
    def __init__(self):
        self.head = None

## INSERTION FUNCTIONS :

# This is a function to insert data list and convert the list into linked-list

    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)

    # This function is to insert a Node at the Begining
    def insert_at_begining(self, data):
        if self.head is None:
            self.head = Node(data, None, None)
            return
        else:
            node = Node(data, self.head, None)
            self.head.prev = node
            self.head = node

    # This function is to insert a Node at the Ending
    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None, None)
            return
        else:
            itr = self.head
            while itr.next:
                itr = itr.next
            itr.next = Node(data, None, itr)

    # This function is to insert a node at a given index
    def insert_at(self, index, data):
        if index < 0 or index >= self.length():
            raise Exception("Invalid Index")

        elif index == 0:
            self.insert_at_begining(data)

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                node = Node(data, itr.next, itr)
                itr.next.prev = node
                itr.next = node
                break
            count += 1
            itr = itr.next

## DELETTING FUNCTIONS :

# This function is used to delete node at begining

    def delete_at_begining(self):
        self.head = self.head.next
        self.head.prev = None

    # This function is used to delete node at end
    def delete_at_end(self):
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.prev.next = itr.next

    # This remove function is used to delete a node at a given index
    def delete_at(self, index):
        if index < 0 or index >= self.length():
            raise Exception("Invalid index")

        elif index == 0:
            self.delete_at_begining()

        count = 0
        itr = self.head
        while itr:
            if index == count:
                itr.prev.next = itr.next
                if itr.next:
                    itr.next.prev = itr.prev
                    break
            itr = itr.next
            count += 1

## Length and Searching Functions :

# This funtion is to get the length of data in Linked List

    def length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count

    # This function is to search the elements in LinkedList
    def Search(self, data):
        if self.head.data == data:
            print(data, "is in LinkedList")
            return
        itr = self.head
        while itr.next:
            if itr.next.data == data:
                print(data, "is in LinkedList")
                return
            itr = itr.next
        print(data, "is not found in LinkedList")


## Printing Funtion of linked lists :

# This function is to print the linked list

    def print_forward(self):
        if self.head == None:
            print("linked list is Empty")
            return

        itr = self.head
        strg = ""
        while itr:
            strg += str(itr.data) + "-->"
            itr = itr.next
        print(strg)

    # This function is to go to the last node of the linked list
    def get_last_node(self):
        itr = self.head
        while itr.next:
            itr = itr.next
        return itr

    # This is a function to print the linked list in reverse order
    def print_backward(self):
        if self.head is None:
            print("Linked list is empty")
            return

        last_node = self.get_last_node()
        itr = last_node
        llstr = ''
        while itr:
            llstr += itr.data + '-->'
            itr = itr.prev
        print("Link list in reverse: ", llstr)

if __name__ == "__main__":
    ll = DoublyLinkedList()
    ## Inserting Nodes
    # Inserting a list of data to make LinkedList
    ll.insert_values(["Banana", "Mango", "Grapes", "Orange"])
    ll.print_forward()
    print()
    # Inserting a Node at Begining of the LinkedList
    ll.insert_at_begining("Begining")
    ll.print_forward()
    print()
    # Inserting a Node at end of the LinkedList
    ll.insert_at_end("Ending")
    ll.print_forward()
    print()
    # Inserting a Node at the specified index of LinkedList
    ll.insert_at(3, "insert_1")
    ll.print_forward()
    print()
    ## Deleting Node
    # Deleting a Node at Begining of the LinkedList
    ll.delete_at_begining()
    ll.print_forward()
    print()
    # Deleting a Node at end of the LinkedList
    ll.delete_at_end()
    ll.print_forward()
    print()
    # Deleting a Node at the specified index of LinkedList
    ll.delete_at(2)
    ll.print_forward()
    print()
    ## Searching in LinkedList and length of LinkedList
    # Printing Length of the LinkedList
    print("Now Length is", ll.length())
    print()
    #Searching for the given value in linkedlist
    ll.Search("Mango")
    print()
    ## Reverse of the linked list
    # Printing Linked list in reverse using doubly linked list
    ll.print_backward()
