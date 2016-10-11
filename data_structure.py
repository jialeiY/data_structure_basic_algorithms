
#Stack class using python list
#support: push,pop,find_min,peek,is_empty,get_size
class Stack(object):
    
    def __init__(self):
        self.stack=[]
        self.__size=0
        self.min_value=[]
    def push(self,item):
        self.stack.append(item)
        self.__size+=1
        if not self.min_value or item<self.min_value[-1]:
            self.min_value.append(item)
    def pop(self):
        if self.is_empty():
            return "empty"

        if self.peek()==self.min_value[-1]:
            self.min_value.pop()
        self.__size-=1
        return self.stack.pop()
    def find_min(self):
        if self.min_value:
            return self.min_value[-1]
    def peek(self):
        if self.is_empty():
            return "empty"
        return self.stack[-1]
    def is_empty(self):
        return self.__size==0
    def get_size(self):
        return self.__size
        
#Queue class using linked list
#support: enqueue,dequeue,is_empty,get_size        
class Queue(object):
    
    class _Node():
        def __init__(self,value):
            self.value=value
            self.next=None
    
    def __init__(self):
        self.length=0
        self.front=None
        self.rear=None
    def enqueue(self,item):
        
        node=self._Node(item)
        if self.length==0:
            self.front=self.rear=node
        else:
            self.rear.next=node
            self.rear=node
        self.length+=1
                            
    def dequeue(self):
        if not self.is_empty():
            temp=self.front
            self.front=self.front.next
            self.length-=1
            if self.length==0:
                self.rear=None
            return temp.value
        else:
            return "queue is empty"
    def is_empty(self):
        return self.length==0
    def get_size(self):
        return self.length

#Deque class using double-linked list
#support: add_front,add_rear,remove_front,remove_rear,is_empty,get_size    
class Deque(object):
    
    class _Node(object):
        def __init__(self,value):
            self.value=value
            self.prev=None
            self.next=None
    
    def __init__(self):
        self.front=None
        self.rear=None
        self.length=0
    def add_front(self,item):
        node=self._Node(item)
        if self.front:
            node.next=self.front
            self.front.prev=node
        self.front=node
        self.length+=1
        if self.length==1:
            self.rear=node
    def add_rear(self,item):
        node=self._Node(item)
        if self.rear:
            self.rear.next=node
            node.prev=self.rear
        self.rear=node
        self.length+=1
        if self.length==1:
            self.front=node
    def remove_front(self):
        node=self.front
        self.front=node.next
        self.length-=1
        if self.length==0:
            self.rear=None
        else:
            self.front.prev=None    
        return node.value
    def remove_rear(self):
        node=self.rear
        self.rear=node.prev
        self.length-=1
        if self.length==0:
            self.front=None
        else:
            self.rear.next=None
        
        return node.value
    def is_empty(self):
        return self.length==0
    def get_size(self):
        return self.length

#Linked List class using double-linked list
#support: append,remove,search,index,insert,pop,is_empty,get_size          
class UnorderedLinkedList(object):
    
    class _Node(object):
        def __init__(self,value):
            self.value=value
            self.next=None
    def __init__(self):
        self.head=None
    def append(self,item):
        node=self._Node(item)
        if not self.head:
            self.head=node
        else:           
            tmp=self.head
            while tmp.next:
                tmp=tmp.next
            tmp.next=node
    def remove(self,item):
        prev=None
        this=self.head
        while this.value!=item and this.next:
            prev=this
            this=this.next        
        if prev==None:
            self.head=this.next
        else:
            prev.next=this.next
    def search(self,item):
        this=self.head
        while this:
            if this.value==item:
                return True
            this=this.next        
        return False
    def is_empty(self):
        return self.head==None
    def get_size(self):
        length=0
        this=self.head
        while this:
            this=this.next
            length+=1
        return length
    def index(self,item):
        pos=0
        this=self.head
        while this:
            if this.value==item:
                return pos
            this=this.next
            pos+=1
        return False
    def insert(self,pos,item):
        node=self._Node(item)
        if pos==0:
            node.next=self.head
            self.head=node
        else:
            this=self.head
            while this and pos>0:
                pos-=1
                prev=this
                this=this.next
            prev.next=node
            node.next=this
    def pop(self,pos=0):
        prev=None
        this=self.head
        while this and pos>0:
            pos-=1
            prev=this
            this=this.next
        if prev==None:
            node=self.head
            self.head=node.next
            return node.value
        prev.next=this.next
        return this.value