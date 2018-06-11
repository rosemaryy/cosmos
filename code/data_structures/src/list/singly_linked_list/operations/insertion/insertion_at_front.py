#Python Utility to add element at the beginning of the Singly Linked List
#Part of Cosmos by OpenGenus Foundation

class Node:
    '''
    A Node in a singly-linked list

    Parameters
    -------------------

    data :
        The data to be stored in the node

    next:
        The link to the next node in the singly-linked list
    '''

    def __init__(self, data=None, next=None):
        ''' Initializes node structure'''
        self.data = data
        self.next = next

    def __repr__(self):
        ''' Node representation as required'''
        return (self.data)

class Singly_Linked_List:
    '''
    A structure of singly linked lists
    '''

    def __init__(self):
        '''Creates a Singly Linked List in O(1) Time'''
        self.head = None
    
    def Insert_In_Front(self,data):
        '''
        Inserts New data at the beginning of the Linked List
        Takes O(1) time
        '''
        self.head=Node(self,data=data,next=self.head)
        

    def __repr__(self):
        '''
        Gives a string representation of the list in the
        given format:

        a -> b -> c -> d
        '''
        AllNodes = []
        current_node = self.head
        while current_node:
            AllNodes.append(str(current_node.data))
            current_node = current_node.next
        if len(AllNodes) > 0:
            return ' -> '.join(AllNodes)
        else:
            return 'Linked List is empty'
