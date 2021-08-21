class Solution:
    def __init__(self):
        self.stack=[]
        self.queue=[]

    def push(self,data):
        self.stack.append(data)

    def pop(self):
        return self.stack.pop()

    def enqueue(self,data):
        self.queue.append(data)

    def dequeue(self):
        return self.queue.pop(0)

    def printAll(self):
        print(self.stack)
        print(self.queue)


q1=Solution()
q1.push(1)
q1.push(2)
q1.push(3)
q1.push(4)
q1.push(5)
q1.enqueue(1)
q1.enqueue(2)
q1.enqueue(3)
q1.enqueue(4)
q1.enqueue(5)
q1.pop()
q1.dequeue()
q1.printAll()
