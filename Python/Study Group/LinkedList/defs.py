class Node():
    def __init__(self,value=None):
        self.data=value
        self.next=None
class LinkedList():
    def __init__(self):
        self.head=None
    def transverse(self):
        if self.head is None:
            print("List has no element")
            return None
        else:
            n = self.head
            while n is not None:
                a=n.data
                print(a)
                n = n.next

    def ins_at_start(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def ins_at_end(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            return None
        n = self.head
        while n.next is not None:
            n = n.next
        n.next = new_node;

    def ins_after_value(self, x, value):

        n = self.head
        while n is not None:
            if n.data == x:
                break
            n = n.next
        if n is None:
            print("Data not in the list")
        else:
            new_node = Node(value)
            new_node.next = n.next
            n.next = new_node

    def insert_before_value(self, x, value):
        if self.head is None:
            print("List has no element")
            return None

        if x == self.head.data:
            new_node = Node(value)
            new_node.next = self.head
            self.head = new_node
            return None

        n = self.head
        while n.next is not None:
            if n.next.data == x:
                break
            n = n.next
        if n.next is None:
            print("item not in the list")
        else:
            new_node = Node(value)
            new_node.next = n.next
            n.next = new_node

    def ins_at_pos(self, pos, value):
        if pos == 1:
            new_node = Node(value)
            new_node.next = self.head
            self.head = new_node
        i = 1
        n = self.head
        while i < pos - 1 and n is not None:
            n = n.next
            i = i + 1
        if n is None:
            print("Index out of bound")
        else:
            new_node = Node(value)
            new_node.next = n.next
            n.next = new_node

    def size(self):
        if self.head is None:
            return 0
        n = self.head
        count = 0
        while n is not None:
            count = count + 1
            n = n.next
        return count

    def search(self, x):
        if self.head is None:
            print("List has no elements")
            return None
        n = self.head
        while n is not None:
            if n.data == x:
                print("Item found")
                return True
            n = n.next
        print("item not found")
        return False
    def del_begin(self):
        if self.head is None:
            print("The list has no element to delete")
            return None
        self.head = self.head.next

    def del_end(self):
        if self.head is None:
            print("The list has no element to delete")
            return None
        n = self.head
        while n.next.next is not None:
            n = n.next
        n.next = None

    def del_value(self, x):
        if self.head is None:
            print("The list has no element to delete")
            return None
        if self.head.data == x:
            self.head = self.head.next
            return None
        n = self.head
        while n.next is not None:
            if n.next.data == x:
                break
            n = n.next
        if n.next is None:
            print("item not found in the list")
        else:
            n.next = n.next.next

if __name__ == '__main__':
    linklist=LinkedList()
    ip=""
    while ip!='12':
        ip=input("Choose one option:\n\t1.Insert at start\n\t2.Insert at end\n\t3.Insert after existing value"
                 "\n\t4.Insert before existing value\n\t5.insert at particular position\n\t6.Display"
                 "\n\t7.Search elements\n\t8.Delete at beginning\n\t9.Delete at end\n\t10.Delete particular value"
                 "\n\t11.Size of Linked List\n\t12.Exit\nEnter one option: ")
        if ip=='1':
            vl=input("Enter the value to be inserted: ")
            linklist.ins_at_start(vl)
        if ip == '2':
            vl = input("Enter the value to be inserted: ")
            linklist.ins_at_end(vl)
        if ip=='3':
            vl = input("Enter the value to be inserted: ")
            x = input("Enter the value to be inserted after: ")
            linklist.ins_after_value(x,vl)
        if ip=='4':
            vl = input("Enter the value to be inserted: ")
            x = input("Enter the value to be inserted before: ")
            linklist.insert_before_value(x,vl)
        if ip=='5':
            vl = input("Enter the value to be inserted: ")
            pos = input("Enter the position the value to be inserted: ")
            linklist.ins_at_pos(int(pos),str(vl))
        if ip=='6':
            linklist.transverse()
        if ip=='7':
            vl = input("Enter the value to be searched: ")
            linklist.search(vl)
        if ip=='8':
            linklist.del_begin()
            linklist.transverse()
        if ip=='9':
            linklist.del_end()
            linklist.transverse()
        if ip=='10':
            vl = input("Enter the value to be deleted: ")
            linklist.del_value(vl)
            linklist.transverse()
        if ip=='11':
            print("Size of the linked list is: "+str(linklist.size()))
        if ip=='12':
            print("End of the Linked List")


