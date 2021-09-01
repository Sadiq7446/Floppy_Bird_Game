""" Python Script to read a linear list of items and store it in an array.
   - Copy the contents from one array to another array
   - Copy the contents from one array to another array in reverse order
   - Delete the duplicate elements from an array. """

# Write your code from here

class Node:
  def __init__(self,data,next) :
    self.data = data
    self.next = next

class Linear_list :
  def  __init__(self):
    self.head = None
  
  # Converting the entered linked list into linear list
  def convrt_list(self, data_list):
    self.head = None
    data = data_list.split("->")
    self.head = data
    print("First array :",data)
  
  # Copy the contents from one array to another array
  def copy_of_array(self) :
    data_2 = self.head
    print("Second array :",data_2)

  # Copy the contents from one array to another array in reverse order
  def copy_in_reverse(self) :
    data_3 = self.head[::-1]
    print ("Reversed array :",data_3)

  # Delete the duplicate elements from an array 
  def delete_dupli(self) :
    data_4 = []
    for i in self.head:
      if i not in data_4 :
        data_4.append(i)
    print("array after removing duplicates :",data_4)

# Using Example values 
if __name__ == '__main__' :
  ll = Linear_list()
  ll.convrt_list("a->a->b->c->c->d->e->e")
  ll.copy_of_array()
  ll.copy_in_reverse()
  ll.delete_dupli()

