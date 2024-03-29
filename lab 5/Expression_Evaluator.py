
class DNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class expEvaluator:
    def __init__(self, exp, a, b, c) -> None:
        self.head = None
        self.exp = exp
        self.length = 0
        self.values = {'a' : a, 'b' : b, 'c' : c}
        self.precedence = {'(' : 0, '+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
        self.checkValidExp(exp)
        self.exp = self.infixToPostfix(self.exp)
        self.evaluatePostfix(self.exp)

    def checkValidExp(self, exp):
        self.setExp(exp)
        self.checkBrackets(self.exp)
        self.checkOps(self.exp)
        
    def setExp(self, exp):
        exp = exp.replace('--', '+').removeprefix('+')
        ops = ['+', '*', '-', '/', '^']
                       
        for i in range(1, len(exp)):
            if exp[i] in ops and exp[i - 1] in ops:
                if exp[i] == '+':
                    exp = exp[:i] + exp[i:].replace('+', ' ', 1)
                    # quit()
                                        
        # for i in range(len(exp)-1):
        #     if exp[i + 1].isalpha() and exp[i] == '-' and i != 0:
        #         self.values[exp[i+1]] =  str(int(self.values[exp[i+1]]) * -1)
        #         self.exp = exp[:i] + exp[i:].replace('-', '', 1)
        self.exp = exp.replace(' ', '')
                
        
    def checkOps(self, exp):
        if len(exp) == 1:
            if exp == 'a':
                print('a')
                print(self.values['a'])
            elif exp == 'b':
                print('b')
                print(self.values['b'])
            elif exp == 'c':
                print('c')
                print(self.values['c'])
            quit()
            
        ops = ['+', '*', '-', '/', '^']       
        for i in range(1, len(exp)):
            if exp[i] in ops and exp[i - 1] in ops and exp[i] != '-':
                print("Error")
                quit()
            elif exp[i].isalpha() and exp[i - 1].isalpha():
                print("Error")
                quit()
            elif (exp[i].isalpha() and exp[i - 1].isdigit()) or (exp[i].isdigit() and exp[i - 1].isalpha()):
                print("Error")
                quit()
                
        if exp[-1] in ops or (exp[0] in ops and exp[0] != '-') or (exp[-2] in ops and exp[-1] == ')'):
            print("Error")
            quit()
            
    def checkBrackets(self, exp):
        open = ['(', '[', '{']
        close = [')', ']', '}']
        for i in range(1, len(exp)):
            if exp[i] in close and exp[i-1] in open:
                print("Error")
                quit()
                
        for ch in exp:
            if ch in open:
                self.push(DNode(ch))
                
            if ch in close:
                if self.isEmpty():
                    print("Error")
                    quit()
                checkBrkt = self.pop()
                if not self.checkMatch(checkBrkt, ch):
                    print("Error")
                    quit()
                
        if not self.isEmpty():
            print("Error")
            quit()
        return True
            
    def checkMatch(self, brkt1, brkt2):
        if brkt1 == '(' and brkt2 == ')':
            return True
        if brkt1 == '[' and brkt2 == ']':
            return True
        if brkt1 == '{' and brkt2 == '}':
            return True
        return False

    def infixToPostfix(self, exp):
        postfix = ""
        for ch in exp:
            if ch.isalpha() or ch.isdigit():
                postfix += ch
            elif ch == '(':
                self.push(DNode(ch))
            elif ch == ')':
                while not self.isEmpty() and self.peek() != '(':
                    postfix += self.pop()
            else:
                while(not self.isEmpty() and self.checkPreced(ch)):
                    postfix += self.pop()
                self.push(DNode(ch))

        while not self.isEmpty():
            postfix += self.pop()
            postfix = postfix.removesuffix('(')

        self.printPostfix(postfix)
        for ch in postfix:
            if ch.isalpha():
                self.push(DNode((ch, self.values[ch])))
            elif ch.isdigit():
                self.push(DNode((ch, ch)))
        return postfix

    def checkPreced(self, ch):
        a = self.precedence[ch]
        b = self.precedence[self.peek()]
        return a <= b

    def evaluatePostfix(self, exp):
        nodes = dict(self.printLS())
        self.clear()
        for char in exp:
            if char.isdigit():
                self.push(DNode(int(nodes[char])))
                continue
            try:
                self.push(DNode(int(nodes[char])))
            except:
                num1 = self.pop()
                num2 = self.pop()
                if num2 is None and char == '-':
                    print(f"{-num1}")
                    return
                self.push(DNode(self.__checkOperation(char, num1, num2)))
        print(self.res)

    def __checkOperation(self, char, num1, num2):
        if char == '+':
            self.res = num1 + num2
        elif char == '-':
            self.res = num2 - num1
        elif char == '*':
            self.res = num1 * num2
        elif char == '/':
            self.res = num2 // num1
        elif char == '^':
            self.res = num2 ** num1
        else:
            print("Error")
            quit()
        return self.res
    
    def printLS(self) -> None:   # print linked list
        currentNode = self.head
        elements = []
        while currentNode is not None:
            elements.append(currentNode.data)
            currentNode = currentNode.next
        return elements

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
            return

        if self.length == 1:
            val = self.head.data
            self.clear()
            return val

        self.length -= 1
        val = self.head.data
        temp = self.head
        self.head = self.head.next
        self.head.prev = None
        temp.next = None
        del temp
        return val

    def clear(self) -> None:
        self.length = 0
        temp = self.head
        while temp is not None:
            self.head = self.head.next
            temp .next = None
            del temp
            temp = self.head

    def peek(self):
        if self.checkError():
            print("Error")
            quit()
        return self.head.data

    def printPostfix(self, exp) -> None:
        print(exp)

    def checkError(self):
        if self.length <= 0:
            return True
        return False

    def isEmpty(self) -> bool:
        return self.length == 0


exp = input()
val1 = input()
val2 = input()
val3 = input()
a = val1[val1.index('=') + 1:]
b = val2[val2.index('=') + 1:]
c = val3[val3.index('=') + 1:]
evaluator = expEvaluator(exp, a, b, c)

# exp = "9+((5+3)*a)^2"
# a = []
# for b in exp:
#     a.append(b)
# print(''.join(a))
    