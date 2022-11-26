from json import loads

class DNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
        
class DoublyLinkedList:
    def __init__(self) -> None:
        self.head = None
        self.prevNode = None    # will be used in case we need access to the node before the current node
        self.__length = 0

    def insertAt(self, newNode: DNode, index: int) -> None:
        if self.checkError(index, self.__length):
            print("Error")
            return
        
        if index == self.__length:   # insert at the end
            self.insertAtEnd(newNode)
            return
        elif index == 0:
            self.insertAtHead(newNode)
            return

        self.__length += 1
        traverse = self.traverseList(index)
        self.prevNode.next = newNode
        newNode.prev = self.prevNode
        newNode.next = traverse
        traverse.prev = newNode

    def insertAtEnd(self, newNode: DNode) -> None:
        self.__length += 1
        if self.head is None:
            self.head = newNode
            return

        lastNode = self.head
        while lastNode.next is not None:
            lastNode = lastNode.next
        lastNode.next = newNode
        newNode.prev = lastNode

    def insertAtHead(self, newNode):
        self.__length += 1
        temp = self.head
        temp.prev = newNode
        newNode.next = temp
        self.head = newNode
        del temp


    def removeAt(self, index: int) -> None:
        if self.checkError(index, self.__length):
            print("Error")
            return
        
        if index == 0:
            self.removeAtHead()
            return
        elif index == self.__length - 1:
            self.removeAtEnd(index)
            return

        self.__length -= 1
        traverse = self.traverseList(index)
        self.prevNode.next = traverse.next
        traverse.next.prev = self.prevNode
        traverse.next = None
        traverse.prev = None
        del traverse

    def removeAtHead(self) -> None:
        self.__length -= 1
        temp = self.head
        self.head = self.head.next
        self.head.prev = None
        temp.next = None
        del temp

    def removeAtEnd(self, index: int):
        self.__length -= 1
        traverse = self.traverseList(index)
        self.prevNode.next = None
        traverse.prev = None
        del traverse
        
    def clear(self) -> None:
        self.__length = 0
        temp = self.head
        while temp is not None:
            self.head = self.head.next
            temp .next = None
            del temp
            temp = self.head

    def get(self, index: int):
        if self.checkError(index, self.__length):
            return "Error"
        
        traverse = self.traverseList(index)
        return traverse.data

    def set(self, data, index: int) -> None:
        if self.checkError(index, self.__length):
            return "Error"
        
        traverse = self.traverseList(index)
        traverse.data = data

    def contains(self, element) -> bool:
        traverse = self.head
        while traverse is not None:
            if traverse.data == str(element):
                return True
            traverse = traverse.next
            
    def traverseList(self, index):   # will be used any time we need to traverse the list till a given index
        traverse, self.prevNode = (self.head,) * 2
        for _ in range(index):
            self.prevNode = traverse
            traverse = traverse.next
        return traverse
    
    def printLS(self) -> None:   # print linked list
        currentNode = self.head
        while currentNode is not None:
            print(currentNode.data)
            currentNode = currentNode.next
            
    def printSubList(self, fromIdx: int, toIdx: int) -> list:
        traverse = self.traverseList(fromIdx)
        elements = []
        while fromIdx <= toIdx:
            elements.append(traverse.data)
            fromIdx += 1
            traverse = traverse.next
        return elements
        
    def checkError(self, index, length, fromIdx=0, toIdx=0):
        checks = [
                  index < 0, index >= length, toIdx < fromIdx,
                  fromIdx < 0, fromIdx >= length,
                  toIdx < 0, toIdx >= length
                 ] 
        if any(checks):
            return True

    @property
    def Size(self) -> int:
        return self.__length

    @property
    def isEmpty(self) -> bool:
        return self.__length == 0
    
DLinkedList = DoublyLinkedList()
elements = loads(input())
operation = input()

for element in elements:
    node = DNode(element)
    DLinkedList.insertAtEnd(node)

