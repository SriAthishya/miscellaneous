class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val

    def add(self, val):
        if self.val:
            if val < self.val:
                if self.left is None:
                    self.left = Node(val)
                else:
                    self.left.add(val)
            elif val > self.val:
                if self.right is None:
                    self.right = Node(val)
                else:
                    self.right.add(val)
        else:
            self.val = val
    '''
    def deleteTree(self,node):
        if (node == None):
            return None
        node.deleteTree(self.left)
        node.deleteTree(self.right)
        print(" Deleting node:", self.val)
    '''

    def height(self,val):
        if val is None:
            return 0
        else:
            lDepth = val.height(val.left)
            rDepth = val.height(val.right)
            if (lDepth > rDepth):
                return lDepth + 1
            else:
                return rDepth + 1

    def DisplayTree(self):
        if self.left:
            self.left.DisplayTree()
        print( self.val)
        if self.right:
            self.right.DisplayTree()

if __name__ == '__main__':
    head = int(input("Enter the root value: "))
    root = Node(head)
    ip=""
    while ip!="4":
        ip=input("Choose one Option:\n\t1.Add values\n\t2.Display the tree\n\t3.Height of the tree"
                 "\n\t4.Exit\nEnter the option: ")
        if ip=="1":
            val=int(input("Enter the value to be added: "))
            root.add(val)
        if ip=='2':
            root.DisplayTree()
        if ip=='3':
            print("Height of the tree is "+str(root.height(root)))
        if ip=='4':
            print("End of the Binary Tree")

#root.deleteTree(root)