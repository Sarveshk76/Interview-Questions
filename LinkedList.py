class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class LL:
    def __init__(self):
        self.head = None

    def insert_start(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_last(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        last = self.head
        while (last.next):
            last = last.next
        last.next = new_node

    def insert_after(self,key,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        curr = self.head
        while(curr):
            if curr.data == key:
                break
            prev = curr
            curr = curr.next
        if curr == None:
            print('Element not exist')
            return
        prev.next = new_node
        new_node.next = curr.next

    def delete_node(self, key):
        if self.head is None:
            print('Linked List is empty')
            return
        temp = self.head
        while (temp is not None):
            if temp.data == key:
                break
            prev = temp
            temp = temp.next
        if temp == None:
            print('Element not exist')
            return
        prev.next = temp.next
        temp = None

    def print_ll(self):
        curr = self.head
        while (curr):
            print(curr.data)
            curr = curr.next
        print('-'*30)

    def reverse(self):
        curr = self.head
        while curr:
            pre = curr
            curr = curr.next
        temp = curr
        curr.next = pre
        

ll = LL()
ll.insert_start(10)
ll.print_ll()
ll.insert_start(20)
ll.print_ll()
ll.insert_last(30)
ll.print_ll()
ll.insert_last(40)
ll.print_ll()
ll.insert_after(30,50)
ll.print_ll()
ll.insert_after(50,60)
ll.print_ll()
ll.delete_node(60)
ll.print_ll()
ll.reverse()