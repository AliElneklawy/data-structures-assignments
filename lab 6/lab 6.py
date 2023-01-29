from json import loads

class Queue:
    def __init__(self, elmnts) -> None:
        self.Q = elmnts
        self.size = len(self.Q)

    def __repr__(self) -> str:
        return str(self.Q)

    def enqueue(self, data) -> None:
        self.size += 1
        self.Q.insert(0, data)

    def dequeue(self) -> None:
        if self.size == 0:
            print("Error")
            quit()
        self.size -= 1
        self.Q.pop()
        
    def Size(self) -> int:
        return self.size

    def isEmpty(self) -> bool:
        return self.size <= 0


elmnts = loads(input())
operation = input()
Q = Queue(elmnts)

if operation == "enqueue":
    data = int(input())
    Q.enqueue(data)
    print(Q)

elif operation == "dequeue":
    Q.dequeue()
    print(Q)

elif operation == "size":
    print(Q.Size())

elif operation == "isEmpty":
    print(Q.isEmpty())

else:
    print("Error")
