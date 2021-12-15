'''                  QUES:2:                 '''
# Implement doubly linked list. The only difference with regular linked list is that dou
# ble linked has prev node reference as well. That way you can iterate in forward and backward direction.
#  Your node class will look this this,
# class Node:
#     def __init__(self, data=None, next=None, prev=None):
#         self.data = data
#         self.next = next
#         self.prev = prev
# Add following new methods,

# def print_forward(self):
#     # This method prints list in forward direction. Use node.next

# def print_backward(self):
#     # Print linked list in reverse direction. Use node.prev for this.
# Implement all other methods in regular linked list class 
# and make necessary changes for doubly linked list (you need to populate node.prev in all those methods)

from typing import Counter


class Node():
    def __init__(self,prev,data,next):
        self.prev=prev
        self.data=data
        self.next=next
class linked_list():
    def __init__(self):
        self.head=None
    
    def insert_at_beginning(self,data):

        if self.head==None:
            self.head=Node(None,data,None)
            return

        self.head=Node(None,data,self.head)

    def insert_at_end(self,data):
        if self.head==None:
            self.head=Node(None,data,None)
            return
        itr=self.head
        while itr.next:
            itr=itr.next
        itr.next=Node(itr,data,None)
        
    def print_forward(self):
        if self.head==None:
            print("the list is empty")
        itr=self.head
        s=''
        while itr:
            s+=(str(itr.data))+'-->'
            itr=itr.next
        print(s)

    def get_last_node(self):
        itr = self.head
        while itr.next:
            itr = itr.next
        return itr
    def print_backward(self):
        if self.head is None:
            print("Linked list is empty")
            return

        itr = self.get_last_node()
        llstr = ''
        while itr:
            llstr+=itr.data + '-->'
            itr = itr.prev
        print(llstr)
    
    def insert_values(self,data_table):
        self.head=None
        for data in data_table:
            self.insert_at_end(data)
    def length(self):
        itr=self.head
        count=0
        while itr:
            count+=1
            itr=itr.next
        print(count)
    
    def remove_at(self,index):
        itr=self.head
        if index==0:
            self.head=self.head.next
        count = 0
        itr = self.head
        while itr:
            if count==index:
                itr.prev.next=itr.next
                itr.next.prev=itr.prev
                break
            count+=1
            itr=itr.next
                

        
ll=linked_list()

ll.insert_at_beginning("orange")
ll.insert_at_beginning("grapes")
ll.insert_at_beginning('mango')
ll.insert_at_beginning('banana')
ll.insert_at_end('figs')
ll.insert_at_end('1')
ll.print_forward()
ll.insert_values(['aam','orange','grapes'])
ll.insert_at_beginning('banana')
ll.insert_at_beginning('gaurav')
ll.insert_at_end('bora')
ll.length()
ll.print_forward()
ll.print_backward()
ll.insert_values(['banana','apple','rusberry'])
ll.remove_at(1)
ll.length()
ll.print_forward()
ll.print_backward()


# class Node:
#     def __init__(self, data=None, next=None, prev=None):
#         self.data = data
#         self.next = next
#         self.prev = prev

# class DoublyLinkedList:
#     def __init__(self):
#         self.head = None

#     def print_forward(self):
#         if self.head is None:
#             print("Linked list is empty")
#             return

#         itr = self.head
#         llstr = ''
#         while itr:
#             llstr += str(itr.data) + ' --> '
#             itr = itr.next
#         print(llstr)

#     def print_backward(self):
#         if self.head is None:
#             print("Linked list is empty")
#             return

#         last_node = self.get_last_node()
#         itr = last_node
#         llstr = ''
#         while itr:
#             llstr += itr.data + '-->'
#             itr = itr.prev
#         print("Link list in reverse: ", llstr)

#     def get_last_node(self):
#         itr = self.head
#         while itr.next:
#             itr = itr.next

#         return itr

#     def get_length(self):
#         count = 0
#         itr = self.head
#         while itr:
#             count+=1
#             itr = itr.next

#         return count

#     def insert_at_begining(self, data):
#         if self.head == None:
#             node = Node(data, self.head, None)
#             self.head = node
#         else:
#             node = Node(data, self.head, None)
#             self.head.prev = node
#             self.head = node

#     def insert_at_end(self, data):
#         if self.head is None:
#             self.head = Node(data, None, None)
#             return

#         itr = self.head

#         while itr.next:
#             itr = itr.next

#         itr.next = Node(data, None, itr)

#     def insert_at(self, index, data):
#         if index<0 or index>self.get_length():
#             raise Exception("Invalid Index")

#         if index==0:
#             self.insert_at_begining(data)
#             return

#         count = 0
#         itr = self.head
#         while itr:
#             if count == index - 1:
#                 node = Node(data, itr.next, itr)
#                 if node.next:
#                     node.next.prev = node
#                 itr.next = node
#                 break

#             itr = itr.next
#             count += 1

#     def remove_at(self, index):
#         if index<0 or index>=self.get_length():
#             raise Exception("Invalid Index")

#         if index==0:
#             self.head = self.head.next
#             self.head.prev = None
#             return

#         count = 0
#         itr = self.head
#         while itr:
#             if count == index:
#                 itr.prev.next = itr.next
#                 if itr.next:
#                     itr.next.prev = itr.prev
#                 break

#             itr = itr.next
#             count+=1

#     def insert_values(self, data_list):
#         self.head = None
#         for data in data_list:
#             self.insert_at_end(data)


# if __name__ == '__main__':
#     ll = DoublyLinkedList()
#     ll.insert_values(["banana","mango","grapes","orange"])
#     ll.print_forward()
#     ll.print_backward()
#     ll.insert_at_end("figs")
#     ll.print_forward()
#     ll.insert_at(0,"jackfruit")
#     ll.print_forward()
#     ll.insert_at(6,"dates")
#     ll.print_forward()
#     ll.insert_at(2,"kiwi")
#     ll.print_forward()