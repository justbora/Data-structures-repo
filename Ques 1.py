
# ll=linked_list()
# # ll.insert_at_beginning(1)
# # ll.insert_at_beginning(2)
# # ll.insert_at_beginning(3)
# # ll.insert_at_beginning(4)
# # ll.insert_at_end(1)
# # ll.insert_at_end(2)
# # ll.insert_at_end(3)
# # ll.insert_at_end(4)
# # ll.length()
# ll.insert_values(["apple",'banana','orange','mango'])
# ll.print()
# ll.remove_at(0)
# ll.print()
# ll.remove_at(2)
# ll.print()

'''                      QUES:1-                        '''
# def insert_after_value(self, data_after, data_to_insert):
#     # Search for first occurance of data_after value in linked list
#     # Now insert data_to_insert after data_after node

# def remove_by_value(self, data):
#     # Remove first node that contains data
# Now make following calls,

#     ll = LinkedList()
#     ll.insert_values(["banana","mango","grapes","orange"])
#     ll.print()
#     ll.insert_after_value("mango","apple") # insert apple after mango
#     ll.print()
#     ll.remove_by_value("orange") # remove orange from linked list
#     ll.print()
#     ll.remove_by_value("figs")
#     ll.print()
#     ll.remove_by_value("banana")
#     ll.remove_by_value("mango")
#     ll.remove_by_value("apple")
#     ll.remove_by_value("grapes")
#     ll.print()


class Node():
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next
#     #
# class linked_list():
#     def __init__(self):
#         self.head=None
    
#     def insert_at_beginning(self,data):
#         node=Node(data,self.head)
#         self.head=node

#     def print(self):
#         if self.head==None:
#             print("The list is empty")
#             return
#         itr=self.head
#         s=""
#         while itr:
#             s+=str(itr.data)+'-->'
#             itr=itr.next
#         print(s)
#     def insert_at_end(self,data):
#         node=Node(data,None)
#         if self.head==None:
#             self.head=node
#             return
#         itr=self.head
#         while itr.next:
#             itr=itr.next
#         itr.next=node
#     def insert_values(self,data_table):
#         # self.head=None
#         for data in data_table:
#             self.insert_at_end(data)
            
#     def length(self):
#         count=0
#         itr=self.head
#         while itr:
#             count+=1
#             itr=itr.next 
#         return count
#         # print("Length:",count) 
#     def remove_at(self,index):
#         if index<0 or index>self.length():
#             print("invalid input")
#         if index==0:
#             self.head=self.head.next
#             return
#         count=0
#         itr=self.head
#         while itr:
#             if count==index-1:
#                 itr.next=itr.next.next
#                 break
#             itr=itr.next
#             count+=1
#     def insert_after_value(self, data_after, data_to_insert):
#         node=Node(data_to_insert,None)
#         itr=self.head
#         while itr:
#             if itr.data==data_after:
#                 node.next=itr.next
#                 itr.next=node
#             itr=itr.next    
#     def remove_by_value(self,data):
#         if self.head==None:
#             return

#         if self.head.data==data:
#             self.head=self.head.next
#             return

#         itr=self.head
#         while itr.next!=None:
#             if itr.next.data==data:
#                 itr.next=itr.next.next
#                 break
#             itr=itr.next

# ll=linked_list()
# ll.insert_values(["banana","mango","grapes","orange"])
# ll.print()
# ll.insert_after_value("mango","apple") # insert apple after mango
# ll.print()
# ll.remove_by_value("orange") # remove orange from linked list
# ll.print()
# ll.remove_by_value("figs")
# ll.print()
# ll.remove_by_value("banana")
# ll.remove_by_value("mango")
# ll.remove_by_value("apple")
# ll.remove_by_value("grapes")
# ll.print()

