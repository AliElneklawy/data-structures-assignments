from json import loads

class SNode:  # singly linked list node.
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self) -> None:
        self.head = None
        self.prevNode = None    # will be used in case we need access to the node before the current node
        self.__length = 0

    def insertAt(self, newNode: SNode, index: int) -> None:
        if self.checkError(index, self.__length):
            print("Error")
            return

        self.__length += 1
        if index == 0:
            self.__insertAtHead(newNode)
            return

        traverse = self.traverseList(index)   # stop at the given index
        newNode.next = traverse
        self.prevNode.next = newNode
        self.printLS()

    def insertAtEnd(self, newNode: SNode) -> None:
        self.__length += 1
        if self.head is None:   # create the first node
            self.head = newNode
            return

        lastNode = self.head
        while lastNode.next is not None:
            lastNode = lastNode.next
        lastNode.next = newNode

    def __insertAtHead(self, newNode: SNode) -> None:
        temp = self.head
        self.head = newNode
        self.head.next = temp
        del temp
        self.printLS()

    def removeAt(self, index: int) -> None:
        if self.checkError(index, self.__length):
            print("Error")
            return

        self.__length -= 1
        if index == 0:
            self.__removeAtHead()
            return

        traverse = self.traverseList(index)   # stop at the given index
        self.prevNode.next = traverse.next
        traverse.next = None
        del traverse
        self.printLS()

    def __removeAtHead(self) -> None:
        temp = self.head
        self.head = self.head.next
        temp.next = None
        del temp
        self.printLS()

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
            print("Error")
            return

        traverse = self.traverseList(index)
        traverse.data = data
        self.printLS()

    def contains(self, element) -> bool:
        traverse = self.head
        while traverse is not None:
            if traverse.data == element:
                return True
            traverse = traverse.next
        return False

    def traverseList(self, index):   # will be used any time we need to traverse the list till a given index
        traverse, self.prevNode = (self.head,) * 2
        for _ in range(index):
            self.prevNode = traverse
            traverse = traverse.next
        return traverse

    def printLS(self) -> None:   # print linked list (used for testing)
        currentNode = self.head
        elements = []
        while currentNode is not None:
            elements.append(currentNode.data)
            currentNode = currentNode.next
        print(elements)

    def printSubList(self, fromIdx: int, toIdx: int) -> list:
        if self.checkError(0, self.__length, fromIdx=fromIdx, toIdx=toIdx):
            print("Error")
            return

        traverse = self.traverseList(fromIdx)
        elements = []
        while fromIdx <= toIdx:
            elements.append(traverse.data)
            fromIdx += 1
            traverse = traverse.next
        print(elements)

    def checkError(self, index, length, fromIdx=0, toIdx=0):
        checks = [
                  index < 0, index >= length, toIdx < fromIdx,
                  fromIdx < 0, fromIdx >= length,
                  toIdx < 0, toIdx >= length
                 ]
        if any(checks):
            return True

    def Size(self) -> int:
        return self.__length

    def isEmpty(self) -> bool:
        return self.__length == 0


Slinkedlist = SinglyLinkedList()  # creating a SinglyLinkedList instance
elements = loads(input())
operation = input()

for element in elements:
    node = SNode(element)
    Slinkedlist.insertAtEnd(node)

if operation == "add":
    Slinkedlist.insertAtEnd(SNode(int(input())))
    Slinkedlist.printLS()

elif operation == "addToIndex":
    index = int(input())
    node = SNode(int(input()))
    Slinkedlist.insertAt(node, index)
    
elif operation == "get":
    index = int(input())
    print(Slinkedlist.get(index))
    
elif operation == "size":
    print(Slinkedlist.Size())
    
elif operation == "set":
    index = int(input())
    data = int(input())
    Slinkedlist.set(data, index)

elif operation == "clear":
    Slinkedlist.clear()
    print([])
    
elif operation == "isEmpty":
    print(Slinkedlist.isEmpty())
    
elif operation == "remove":
    index = int(input())
    Slinkedlist.removeAt(index)

elif operation == "sublist":
    fromIdx = int(input())
    toIdx = int(input())
    Slinkedlist.printSubList(fromIdx, toIdx)
    
elif operation == "contains":
    elmnt = int(input())
    print(Slinkedlist.contains(elmnt))
    
        # =================================================================================================== #
        
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
        self.printLS()

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
        self.printLS()


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
        self.printLS()

    def removeAtHead(self) -> None:
        self.__length -= 1
        temp = self.head
        self.head = self.head.next
        self.head.prev = None
        temp.next = None
        del temp
        self.printLS()

    def removeAtEnd(self, index: int):
        self.__length -= 1
        traverse = self.traverseList(index)
        self.prevNode.next = None
        traverse.prev = None
        del traverse
        self.printLS()
        
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
            print("Error")
            return
        
        traverse = self.traverseList(index)
        traverse.data = data
        self.printLS()

    def contains(self, element) -> bool:
        traverse = self.head
        while traverse is not None:
            if traverse.data == element:
                return True
            traverse = traverse.next
        return False
            
    def traverseList(self, index):   # will be used any time we need to traverse the list till a given index
        traverse, self.prevNode = (self.head,) * 2
        for _ in range(index):
            self.prevNode = traverse
            traverse = traverse.next
        return traverse
    
    def printLS(self) -> None:   # print linked list
        currentNode = self.head
        elements = []
        while currentNode is not None:
            elements.append(currentNode.data)
            currentNode = currentNode.next
        print(elements)
            
    def printSubList(self, fromIdx: int, toIdx: int) -> list:
        if self.checkError(0, self.__length, fromIdx=fromIdx, toIdx=toIdx):
            print("Error")
            return
        
        traverse = self.traverseList(fromIdx)
        elements = []
        while fromIdx <= toIdx:
            elements.append(traverse.data)
            fromIdx += 1
            traverse = traverse.next
        print(elements)
        
    def checkError(self, index, length, fromIdx=0, toIdx=0):
        checks = [
                  index < 0, index >= length, toIdx < fromIdx,
                  fromIdx < 0, fromIdx >= length,
                  toIdx < 0, toIdx >= length
                 ] 
        if any(checks):
            return True

    def Size(self) -> int:
        return self.__length

    def isEmpty(self) -> bool:
        return self.__length == 0
  
  
DLinkedList = DoublyLinkedList()  
elements = loads(input())
operation = input()

for element in elements:
    node = DNode(element)
    DLinkedList.insertAtEnd(node)

if operation == "add":
    DLinkedList.insertAtEnd(DNode(int(input())))
    DLinkedList.printLS()

elif operation == "addToIndex":
    index = int(input())
    node = DNode(int(input()))
    DLinkedList.insertAt(node, index)
    
elif operation == "get":
    index = int(input())
    print(DLinkedList.get(index))
    
elif operation == "size":
    print(DLinkedList.Size())
    
elif operation == "set":
    index = int(input())
    data = int(input())
    DLinkedList.set(data, index)

elif operation == "clear":
    DLinkedList.clear()
    print([])
    
elif operation == "isEmpty":
    print(DLinkedList.isEmpty())
    
elif operation == "remove":
    index = int(input())
    DLinkedList.removeAt(index)

elif operation == "sublist":
    fromIdx = int(input())
    toIdx = int(input())
    DLinkedList.printSubList(fromIdx, toIdx)
    
elif operation == "contains":
    elmnt = int(input())
    print(DLinkedList.contains(elmnt))


        # ==================================================================================================== #
        
        
from json import loads


class SNode:  # singly linked list node.
    def __init__(self, coeff):
        self.coeff = coeff
        self.next = None

class SinglyLinkedList:
    def __init__(self) -> None:
        self.head = None
        self.prevNode = None    # will be used in case we need access to the node before the current node
        self.__length = 0

    def insertAtEnd(self, newNode: SNode) -> None:
        self.__length += 1
        if self.head is None:   # create the first node
            self.head = newNode
            return

        lastNode = self.head
        while lastNode.next is not None:
            lastNode = lastNode.next
        lastNode.next = newNode

    def clear(self) -> None:
        self.__length = 0
        temp = self.head
        while temp is not None:
            self.head = self.head.next
            temp .next = None
            del temp
            temp = self.head

    def printLS(self) -> None:
        currentNode = self.head
        elements = []
        while currentNode is not None:
            elements.append(currentNode.coeff)
            currentNode = currentNode.next
        return elements

    def Size(self) -> int:
        return self.__length


def checkError(poly1="A", poly2="A"):
    if (poly1 not in polyNamesList) or (poly2 not in polyNamesList):
        return True
    return False


def setPolynomial(polyName, coeff):
    polyNamesList.append(polyName)
    if polyName == "A":
        for coefficient in coeff:
            A.insertAtEnd(SNode(coefficient))
            
        if A.Size() == 0:
            print("Error")
            return
        
        polynomials.append((polyName, A))

    elif polyName == "B":
        for coefficient in coeff:
            B.insertAtEnd(SNode(coefficient))
        
        if B.Size() == 0:
            print("Error")
            return
        
        polynomials.append((polyName, B))

    elif polyName == "C":
        for coefficient in coeff:
            C.insertAtEnd(SNode(coefficient))
            
        if C.Size() == 0:
            print("Error")
            return
        
        polynomials.append((polyName, C))

    else:
        print("Error")


def printPolynomial(polyName, lstOrInst):
    polynomialStr = ""
    for requiredList in polynomials:
        if requiredList[0] == polyName:

            if lstOrInst == "lst":
                 PN = requiredList[1]
            else:
                PN = requiredList[1].printLS()

            for i in range(len(PN)):
                PN[i] = str(PN[i])
                if PN[i][0] != "-" and i != 0:
                    PN[i] = "+" + PN[i]

            degree = len(PN) - 1
            for i in range(len(PN)):
                if PN[i] == "-1":
                    PN[i] = "-"

                elif PN[i] == "+1" or PN[i] == "1":
                    if i == 0:
                        PN[i] = ""

                    else:
                        PN[i] = "+"

                if degree == 0:
                    polynomialStr += f"{PN[i]}"
                    break

                elif degree == 1:
                    polynomialStr += f"{PN[i]}x"

                else:
                    polynomialStr += f"{PN[i]}x^{degree}"
                degree -= 1

    print(polynomialStr)

def subAddPolys(poly1, poly2, operation):

    if checkError(poly1, poly2):
        print("Error")
        return

    result = []
    firstPoly = []
    scndPoly = []

    for poly in polynomials:
        if poly[0] == poly1:
            firstPoly = poly[1].printLS()   # save poly1 in firstPoly
        elif poly[0] == poly2:
            scndPoly = poly[1].printLS()

    lenDiff = abs(len(firstPoly) - len(scndPoly))   # make the polynomilas of the same length
    if len(firstPoly) > len(scndPoly):
        for _ in range(lenDiff):
            scndPoly.insert(0, 0)
    else:
        for _ in range(lenDiff):
            firstPoly.insert(0, 0)

    if operation == "add":
        for i in range(len(firstPoly)):
            result.append(firstPoly[i] + scndPoly[i])
    else:
        for i in range(len(firstPoly)):
            result.append(firstPoly[i] - scndPoly[i])
               
    R = list(filter((0).__ne__, result))   # remove all the zeros
    polynomials.append(("R", R))
    printPolynomial("R", "lst")
    polynomials.pop()    # remove the last added element


def mulPolys(poly1, poly2):

    if checkError(poly1, poly2):
        print("Error")
        return

    firstPoly = []
    scndPoly = []

    for poly in polynomials:
        if poly[0] == poly1:
            firstPoly = poly[1].printLS()   # save poly1 in firstPoly
        elif poly[0] == poly2:
            scndPoly = poly[1].printLS()

    result = [0] * (len(firstPoly) + len(scndPoly) - 1)   # length of the resultant array = length of the first one + length of the scnd - 1
    for i, term1 in enumerate(firstPoly):
        for j, term2 in enumerate(scndPoly):
            result[i + j] += term1 * term2

    polynomials.append(("R", result))
    printPolynomial("R", "lst")
    polynomials.pop()

def clear(polyName):

    if checkError(polyName):
        print("Error")
        return

    for poly in polynomials:
        if poly[0] == polyName:
            if not poly[1].Size():
                print("Error")
                return
            
            poly[1].clear()
            print([])
            return

def eval(polyName, value):

    if checkError(polyName):
        print("Error")
        return

    for poly in polynomials:
        if poly[0] == polyName:
            polyList = poly[1].printLS()
            break
    
    degree = len(polyList) - 1
    R = 0
    for term in polyList:
        R += term * (value ** degree)
        degree -= 1

    print(int(R))

A = SinglyLinkedList()
B = SinglyLinkedList()
C = SinglyLinkedList()
polynomials = []  # will be used to store the polynomial object and its name
polyNamesList = []   # will be used for error checking

try:
    while True:
        try:
            operation = input()
        except:
            break
        
        if operation == "set":
            polyName = input()
            coeff = loads(input())
            if len(coeff) == 0:
                print("Error")
                break
            setPolynomial(polyName, coeff)

        elif operation == "print":
            polyName = input()
            printPolynomial(polyName, "inst")

        elif operation == "add":
            poly1Name = input()
            poly2Name = input()
            subAddPolys(poly1Name, poly2Name, "add")

        elif operation == "sub":
            poly1Name = input()
            poly2Name = input()
            subAddPolys(poly1Name, poly2Name, "sub")

        elif operation == "mult":
            poly1Name = input()
            poly2Name = input()
            mulPolys(poly1Name, poly2Name)

        elif operation == "clear":
            polyName = input()
            clear(polyName)

        elif operation == "eval":
            polyName = input()
            value = float(input())
            eval(polyName, value)
            
        else:
            print("Error")
            break
except:
    print("Error")
