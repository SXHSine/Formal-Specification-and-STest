class Node(object):
    def __init__(self,val,p=0):
        self.data = val
        self.next = p

class LinkList(object):
    def __init__(self):
        self.head=0

    def initList(self,data):
        self.head = Node(data[0])
        p = self.head
        for i in data[1:]:
            node = Node(i)
            p.next = node
            p = p.next


    def getLength(self):
        p = self.head
        length = 0
        while p!=0:
            length+=1
            p = p.next
        return length

    def is_empty(self):
        if self.getLength()==0:
            return True
        else:
            return False
    
    def clear(self):
        self.head=0

    def append(self,item):
        q = Node(item)
        if self.head==0:
            self.head = q
        else:
            p = self.head
            while p.next!=0:
                p = p.next
            p.next = q

    def getItem(self,index):
        if self.is_empty():
            print('LinkList is empty')
            return 
        j=0
        p = self.head
        while p.next!=0 and j<index:
            p = p.next
            j += 1
        if j==index:
            return p.data
        else:
            print('target is not exsit')

    def insert(self,index,item):
        if(self.is_empty() or index<0 or index>self.getLength()):
            print('LinkList is not long enough')
            return
        if index==0:
            q = Node(item,self.head)
            self.head = q
        p = self.head
        post = self.head
        j = 0
        while p.next!=0 and j<index:
            post = p
            p = p.next
            j+=1
        if index==j:
            post.next = Node(item,p)
            # q = Node(item,p)
            # post.next = q
            # q.next = p
        
    def delete(self,index):
        if self.is_empty() or index<0 or index>self.getLength():
            print('The node is not exist!')
            return
        if index==0:
            self.head = self.head.next
            return
        p = self.head
        post = self.head
        j=0
        while p.next!=0 and j<index:
            post = p
            p = p.next
            j += 1
        if index==j:
            post.next=p.next
        

    def index(self,value):
        if self.is_empty():
            print('LinkList is empty')
            return
        p = self.head
        i=0
        while p.next!=0 and not p.data!=value:
            p = p.next
            i+=1
        if p.data==value:
            return 1
        else:
            return -1

    def __getItem__(self,key):
        if self.is_empty():
            print('LinkList is empty')
            return
        elif key<0 or key>self.getLength():
            print('the given key is error')
            return
        else:
            return self.getItem(key)

    def __setItem__(self,key,value):
        if self.is_empty():
            print('LinkList is empty')
            return
        elif key<0 or key>self.getLength():
            print('the key is error')
            return
        else:
            self.delete(key)
            return self.insert(key,value)

l = LinkList()
l.initList([1,2,3,4,5])
# print(l.getItem(3))

# l.insert(4,50)
# print(l.getItem(4))        

# l.append(60)
# print(l.getItem(6))

l.delete(4)
l.append(60)
print(l.getItem(4))