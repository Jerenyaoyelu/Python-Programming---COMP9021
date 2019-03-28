# Written by **** for COMP9021

from linked_list_adt import *

class ExtendedLinkedList(LinkedList):
    def __init__(self, L = None):
        super().__init__(L)

    def rearrange(self, step):
        New = None
        visited_nodes_dict = {}
        check_nodes_dict = {}
        t=self.head
        while t.next_node !=None:
            check_nodes_dict.setdefault(id(t),1)
            t = t.next_node
        check_nodes_dict.setdefault(id(t),1)
        print(check_nodes_dict)
        if self.head == None:
            return
        if self.head.next_node == None:
            return self.head
        current_1 = self.head
        while True:
            count_step = 0
            if visited_nodes_dict == {}:
                count_step += 1
            while count_step < step:
                if current_1.next_node != None:
                    current_1 = current_1.next_node
                else:
                    current_1 = self.head
                count_step += 1
            visited_nodes_dict.setdefault(id(current_1),1)
            if visited_nodes_dict == check_nodes_dict:
                print(visited_nodes_dict)
                break
        if visited_nodes_dict == check_nodes_dict:
            current_1 = self.head
            New_head = None
            for e in visited_nodes_dict:
                while True:
                    if id(current_1.next_node) !=e and current_1.next_node != None:
                        current_1 = current_1.next_node
                    elif id(current_1.next_node) ==e:
                        if New_head == None:
                            current_2 = current_1.next_node
                            current_1.next_node = current_2.next_node
                            New_head = current_2
                            break
                        else:
                            current_2.next_node = current_1.next_node
                            current_2 = current_2.next_node
                            current_1.next_node = current_2.next_node
                            break
                    else:
                        current_1.next_node = self.head
            if current_2 == current_2.next_node:
                current_2.next_node = None
                self.head = New_head
            
                        
    
