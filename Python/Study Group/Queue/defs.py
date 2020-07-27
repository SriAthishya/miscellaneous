class Queue():
    def __init__(self):
        self.queue=[]
    def enqueue(self,value):
        self.queue.append(value)
    def dequeue(self):
        return self.queue.pop(0)
    def front(self):
        return self.queue[0]
    def rear(self):
        return self.queue[-1]
    def display(self):
        return self.queue
if __name__ == '__main__':
    que=Queue()
    ip=""
    while ip!="6":
        ip=input("Choose one option\n\t1.Add an element\n\t2.Display the Front element\n\t"
                 "3.Display the Rear element\n\t4.Display the full Queue\n\t5.Remove an element\n\t6.exit\n"
                 "Enter any one option: ")
        if ip=='1':
            value=input("Element to be enqueued: ")
            que.enqueue(value)
        if ip=='2':
            print("Front element is "+str(que.front()))
        if ip=='3':
            print("Front element is "+str(que.rear()))
        if ip=='4':
            print(que.display())
        if ip=='5':
            print(str(que.dequeue())+" is removed from the Queue")
        if ip=='6':
            print("End of the Queue Operation")
