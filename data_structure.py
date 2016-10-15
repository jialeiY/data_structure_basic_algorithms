
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
        
#minimum binary heap using python list
#support: insert,find_min,del_min,is_empty,get_size,build_heap
class Min_BinaryHeap(object):
    def __init__(self):
        self.heap=[0]
        self.length=0
    def _swim(self):
        i=self.length
        while i>1 and self.heap[i]<self.heap[i/2]:
            self.heap[i/2],self.heap[i]=self.heap[i],self.heap[i/2]
            i/=2
    def _sink(self):
        i=1
        while 2*i<=self.length:
            j=2*i
            if j<self.length and self.heap[j]>self.heap[j+1]:
                j+=1
            if self.heap[i]<=self.heap[j]:
                break
            self.heap[i],self.heap[j]=self.heap[j],self.heap[i]
            i=j
                                  
    def insert(self,key):
        self.length+=1
        if self.length>=len(self.heap):
            self.heap.append(key)
        else:
            self.heap[self.length]=key

        self._swim()
    def find_min(self):
        return self.heap[1]
    def del_min(self):
        if self.is_empty():
            return "empty"
        smallest=self.heap[1]
        self.heap[1]=self.heap[self.length]
        self.heap[self.length]=None
        self.length-=1
        self._sink()
        return smallest
    def is_empty(self):
        return self.length==0
    def get_size(self):
        return self.length
    def build_heap(self,the_list):
        for k in the_list:
            self.insert(k)

#Hash table
#support: put,get,hash_function       
class HashTable(object):
    class _Node(object):
        def __init__(self,key,value):
            self.key=key
            self.value=value
            self.next=None
    def __init__(self,table_size=11):
        self.table_size=table_size
        self.slots=[None]*table_size
    def hash_function(self,key):
        return key % self.table_size
    def put(self,key,val):
        hash_value=self.hash_function(key)
        node=self._Node(key,val)
        if self.slots[hash_value]:
            tmp_node=self.slots[hash_value]
            while tmp_node.next:
                tmp_node=tmp_node.next
            tmp_node.next=node
        else:
            self.slots[hash_value]=node
            
    def get(self,key):
        hash_value=self.hash_function(key)
        tmp_node=self.slots[hash_value]
        while tmp_node and tmp_node.key!=key:
            tmp_node=tmp_node.next
        if tmp_node:
            return tmp_node.value
        return "no key value"
    def __getitem__(self,key):
        return self.get(key)
    def __setitem__(self,key,value):
        self.put(key,value)
    def __len__(self):
        count=0
        for e in self.slots:
            if e:
                tmp_node=e
                while tmp_node:
                    count+=1
                    tmp_node=tmp_node.next
        return count
    def __contains__(self,key):
        hash_value=self.hash_function(key)
        tmp_node=self.slots[hash_value]
        while tmp_node and tmp_node.key!=key:
            tmp_node=tmp_node.next
        if tmp_node:
            return True
        return False

#Binary Search Tree
#support: put,get,delete,find_min,find_rank,search_by_rank,is_empty,get_size            
class BinarySearchTree(object):
    class _TreeNode(object):
        def __init__(self,key,value):
            self.key=key
            self.value=value
            self.left=None
            self.right=None
            self.node_num=1
    def __init__(self):
        self.root=None
    def is_empty(self):
        return self.get_size()==0
    def get_size(self):
        if self.root:
            return self.root.node_num
        return 0
    def __contains__(self,key):
        return self.get(key)!=None
    def put(self,key,value):
        if not self.root:
            self.root=self._TreeNode(key,value)
        else:
            self._put(key,value,node=self.root)
    def _put(self,key,value,node):       
            node.node_num+=1
            if key<node.key:
                if node.left:
                    self._put(key,value,node.left)
                else:
                    node.left=self._TreeNode(key,value)
            elif key>node.key:
                if node.right:
                    self._put(key,value,node.right)
                else:
                    node.right=self._TreeNode(key,value)
            else:
                node.value=value
    def get(self,key):
        return self._get(key,self.root)
    def _get(self,key,node):
        if not node:
            return None
        if key<node.key:
            return self._get(key,node.left)
        elif key>node.key:
            return self._get(key,node.right)
        else:
            return node.value            
    def delete(self,key):
        self.root=self._delete(key,self.root)
    def _delete(self,key,node):
        if not node:
            return None
        if key<node.key:
            node.left=self._delete(key,node.left)
        elif key>node.key:
            node.right=self._delete(key,node.right)
        else:
            if not node.left:
                return node.right
            if not node.right:
                return node.left
            x=self._find_min(node.right)
            x.right=self._delete(x.key,node.right)
            x.left=node.left
            node=x
        node.node_num=(node.left.node_num if node.left else 0)+ \
        (node.right.node_num if node.right else 0)+1
        return node                        
    def find_min(self):
        if self.is_empty():
            return None
        return self._find_min(self.root).key
    def _find_min(self,node):
        while node.left:
            node=node.left
        return node
    def find_rank(self,key):
        return self._find_rank(key,self.root)
    def _find_rank(self,key,node):
        if not node:
            return None
        if key<node.key:
            return self._find_rank(key,node.left)
        elif key>node.key:
            rank=self._find_rank(key,node.right)
            if rank:
                return rank+(node.left.node_num if node.left else 0)+1
            return None
        else:
            return (node.left.node_num if node.left else 0)+1

    def search_by_rank(self,rank):
        if rank>self.get_size() or rank==0:
            return None
        return self._search_by_rank(rank,self.root).key
    def _search_by_rank(self,rank,node):
        left_size=(node.left.node_num if node.left else 0)+1
        if rank<left_size:
            return self._search_by_rank(rank,node.left)
        elif rank>left_size:
            return self._search_by_rank(rank-left_size,node.right)
        else:
            return node

#graph
#support: add_vertex,add_edge,get_vertex,get_vertices
#also support: "in" operation and loop      
class Graph(object):
    def __init__(self):
        self.vert_list={}
        
    def add_vertex(self,v):
        if v not in self.vert_list:
            self.vert_list[v]={}
    def add_edge(self,from_v,to_v,weight=0):
        if not from_v in self.vert_list:
            self.add_vertex(from_v)
        if not to_v in self.vert_list:
            self.add_vertex(to_v)
        self.vert_list[from_v][to_v]=weight
    def get_vertex(self,v_key):
        return self.vert_list.get(v_key,None)
    def get_vertices(self):
        return self.vert_list.keys()
    def __contains__(self,v):
        return v in self.vert_list
    def __iter__(self):
        return iter(self.vert_list.values())
