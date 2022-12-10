from json import loads

class DNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
        
class Stack:
    def __init__(self, arr) -> None:
        self.head = None
        self.length = 0
        for elmnt in reversed(arr):
            self.push(DNode(elmnt))

    def push(self, newNode):
        self.length += 1
        if self.head is None:
            self.head = newNode
            return
        
        temp = self.head
        temp.prev = newNode
        newNode.next = temp
        self.head = newNode
        del temp

    def pop(self) -> None:
        if self.checkError():
            print("Error")
            return
        
        if self.length == 1:
            self.clear()
            print("[]")
            return
        
        self.length -= 1
        val = self.head.data
        temp = self.head
        self.head = self.head.next
        self.head.prev = None
        temp.next = None
        del temp
        self.printStack()
        return val
        
    def peek(self):
        if self.checkError():
            return "Error"
        return self.head.data
    
    def printStack(self) -> None:   # print linked list
        currentNode = self.head
        elements = []
        while currentNode is not None:
            elements.append(currentNode.data)
            currentNode = currentNode.next
        print(elements)
        
    def clear(self) -> None:
        self.length = 0
        temp = self.head
        while temp is not None:
            self.head = self.head.next
            temp .next = None
            del temp
            temp = self.head
        
    def checkError(self):
        if self.length <= 0:
            return True
        return False

    def Size(self) -> int:
        return self.length

    def isEmpty(self) -> bool:
        return self.length == 0
  
  
arr = loads(input())
s = Stack(arr)
operation = input()

if operation == "push":
    s.push(DNode(int(input())))
    s.printStack()
    
elif operation == "pop":
    val = s.pop()
    
elif operation == "peek":
    print(s.peek())

elif operation == "isEmpty":
    print(s.isEmpty())
    
elif operation == "size":
    print(s.Size())

