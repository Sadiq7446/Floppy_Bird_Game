""" Python Script to create a Circular singly linked list for adding and 
deleting a Node. """

# Write your code from here

# Creating a Node class to use in Linked list
class Node :
  def __init__(self,data,next) :
    self.data = data
    self.next = next

# Creating a Circular_Linked_List class to make a circular linked list
class Circular_Linked_List :
  def __init__(self) :
    self.head = None

# Inserting a data list for example of circular linked list
  def insert_list (self, data_list) :
    self.head = None
    for data in data_list :
      self.insert_at_end(data)
    self.Circular_link()
  
  # Inserting the given data at the end of the example list
  def insert_at_end(self,data):
    if self.head == None:
      self.head = Node(data,self.head)
      return
    itr = self.head
    while itr.next :
      itr = itr.next
    itr.next = Node(data,None)   
  
  # This function creates a link to the first node and creates a circular list
  def Circular_link (self):
    itr = self.head
    temp = self.head
    while itr.next :
      itr = itr.next
    itr.next = temp 
  
  # This function is used to print and show the output
  def print(self) :
    if self.head is None :
      print("Linked list is Empty")
      return
    itr = self.head
    temp = self.head
    llstr = ''
    while itr :
      if itr.next == temp :
          llstr += str(itr.data) + "-->"
          break
      llstr += str(itr.data) + "-->"
      itr = itr.next
    print(llstr)

  # Length of the present list
  def length(self) :
    count = 0
    itr = self.head
    temp = self.head
    while itr :
      if itr.next == temp :
        count += 1
        break
      count += 1
      itr = itr.next
    return count
  
  # This function is to Insert given data at the given index
  def insert_at(self,index,data) :
    if index<0 or index >= self.length():
      raise Exception("Invalid index")
    if index == 0 :
      self.head = Node(data, self.head)
      return    
    count = 0 
    itr = self.head
    while itr:
      if count == index-1 :
        node = Node(data,itr.next)
        itr.next = node
        break
      itr = itr.next
      count += 1
  
  # This function is to delete the data at the given index 
  def delete_at(self,index):
    if index<0 or index >= self.length():
      raise Exception("Invalid index")
    if index == 0 :
      self.head = self.head.next
      return
    count = 0
    itr = self.head
    while itr :
      if count == index-1 :
        itr.next = itr.next.next
        break
      itr = itr.next
      count += 1    


if __name__ == '__main__' :
  ll = Circular_Linked_List()
  # Inserting the list of data as example
  ll.insert_list([0,9,8,7,6,5,4,3,2,1])
  ll.print()
  print()
  # Printing the length of list
  print("Length of list is : ",ll.length())
  print()
  # Insert a value at the given index
  ll.insert_at(2,"Odd_Data")
  ll.print()
  print()
  # Deletting a value from the givenn index
  ll.delete_at(2)
  ll.print()

