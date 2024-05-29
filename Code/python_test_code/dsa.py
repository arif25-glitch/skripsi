class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class LinkedList:
    def __init__(self):
        self.__head = None
        self.__current = None
        self.length = 0
        self.__tail = None
    
    def __zeroInsert(self, data):
        node = Node(data)
        self.__head = node
        self.__tail = node
        self.__current = node
        
    def add(self, data):
        if self.__head == None:
            self.__zeroInsert(data)
        else:
            node = Node(data)
            node.next = self.__current
            self.__head.prev = node
            self.__head = node
            self.__current = node
            
        self.length += 1
    
    def insert(self, data, index=0):
        if index <= 0:
            self.add(data)
        elif index > self.length - 1:
            if self.__tail == None:
                self.__zeroInsert(data)
            else:
                node = Node(data)
                node.prev = self.__tail
                self.__tail.next = node
                self.__tail = node
                self.__current = self.__head
        else:
            self.resetCurrent()
            node = Node(data)
            for i in range(index):
                self.next()
            node.next = self.__current
            node.prev = self.__current.prev
            self.__current.prev.next = node
            self.__current.prev = node
            self.resetCurrent()
        self.length += 1
    
    def remove(self, index=0):
        self.resetCurrent()
        for i in range(index):
            self.next()
        self.__current.prev.next = self.__current.next
        self.__current.next.prev = self.__current.prev
        self.length -= 1
        self.resetCurrent()
    
    def change(self, data, index=0):
        self.resetCurrent()
        for i in range(index):
            self.next()
        self.__current.data = data
        self.resetCurrent()
    
    def next(self):
        if self.__current.next != None:
            self.__current = self.__current.next
            return self.__current
        else:
            print("End Of Nodes")

    def prev(self):
        if self.__current.prev != None:
            self.__current = self.__current.prev
            return self.__current
        else:
            print("End Of Nodes")
    
    def getHeadData(self):
        return self.__head.data
    def getHead(self):
        return self.__head
    def getTail(self):
        return self.__tail
    def getTailData(self):
        return self.__tail.data
    def getCurrentData(self):
        return self.__current.data
    def getCurrent(self):
        return self.__current
    def setCurrent(self, node):
        self.__current = node
    
    def resetCurrent(self):
        self.__current = self.__head

if __name__ == "__main__":
    test = LinkedList()
    test.add(12)
    test.add(15)
    test.add(17)
    test.add(18)
    test.add(19)
    test.add(10)
    test.add(1)
    test.insert(500, 3)
    test.insert('forever nakal', 3)
    test.insert([1, 2, 3, 4, 5, 6, 7], 0)
    test.change('yaya', 2)
    test.change('yoyo', 7)
    print("=========================")
    print("=========================")
    for i in range(test.length):
        print(test.getCurrentData())
        test.next()
    test.remove(3)
    test.change('jangan nakal', 3)
    test.change('19', 2)
    test.setCurrent(test.getTail())
    for i in range(test.length):
        print(test.getCurrentData())
        test.prev()