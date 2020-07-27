class Stack():
    def __init__(self):
        self.stack=[]
    def is_empty(self):
        return self.stack==[]
    def push(self, inp):
        self.stack.append(inp)
    def pop(self):
        return self.stack.pop(-1)
    def top(self):
        if self.is_empty():
            print("Stack is empty!")
            return None
        else:
            return self.stack[-1]
    def size(self):
        return len(self.stack)
    def display(self):
        return self.stack
if __name__ == '__main__':
    stck=Stack()
    ip=""
    while ip!="6":
        ip=input("Choose one option\n\t1.Add an element\n\t2.Size of the stack\n\t"
                 "3.Display the Top element\n\t4.Display the full stack\n\t5.Remove an element\n\t6.exit\n"
                 "Enter any one option: ")
        if ip=='1':
            value=input("Element to be pushed: ")
            stck.push(value)
        if ip=='2':
            print("Size of Stack is "+str(stck.size()))
        if ip=='3':
            print(str(stck.top())+" is in the first position")
        if ip=='4':
            print(stck.display())
        if ip=='5':
            print(str(stck.pop())+" is removed from the stack")
        if ip=='6':
            print("End of the Stack Operation")








