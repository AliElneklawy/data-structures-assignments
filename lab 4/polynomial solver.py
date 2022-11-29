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
