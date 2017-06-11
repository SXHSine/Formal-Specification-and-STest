class Edge(object):
    def __init__(self,adjvex,seq,nextEdge=None):
        self.adjvex = adjvex
        self.seq = seq
        self.next = nextEdge

class Vertex(object):
    def __init__(self,seq,link=None):
        self.seq = seq
        self.link = link

class Adjlist(object):
    def __init__(self,size=0,list=None):
        self.size = size
        self.list = list

    # def createAdjList(self,size):
    #     adjList = Adjlist(size)
    #     adjList.list = []
    #     # adjList.list = size*Vertex(0)
    #     for i in range(0,size):
    #         vertex = Vertex(i)
    #         adjList.list.append(vertex)
    #         # print(adjList.list[i].seq+' ')
    #     return adjList

    def createAdjList(self,size,l):
        adjList = Adjlist(size)
        adjList.list = []
        # adjList.list = size*Vertex(0)
        for i in range(0,len(l)):
            vertex = Vertex(l[i])
            adjList.list.append(vertex)
            # print(str(adjList.list[i].seq)+' ')
        return adjList
    
    def insertEdge(self,seq,head,end):
        rear = head.link            #每个顶点可以有N个边
        newEdge = Edge(end,seq)
        if rear==None:
            head.link = newEdge
        else:
            while rear.next!=None:
                rear = rear.next
            rear.next = newEdge

    def findTheVertex(self,seq,adjList):
        for i in range(0,len(adjList.list)):
            if adjList.list[i].seq==seq:
                print('findTheVertex:'+str(i))
                return i
        return -1
    
    def findTheEdgeNextVerSeq(self,edgeSeq,adjList):
        for i in range(0,len(adjList.list)):
            rear = adjList.list[i].link
            while rear!=None:
                if rear.seq==edgeSeq:
                    print('findTheEdgeNextVerSeq:  '+str(adjList.list[rear.adjvex].seq))
                    return adjList.list[rear.adjvex].seq
                rear = rear.next
        return -1


results=[]
def printPath(path,AdjList):
    # i = 0
    # while path[i+1]!=0:
    #     print(str(path[i])+' ',end='')
    #     i+=1
    # print(path[i])
    # print('\n------')
    result = str(AdjList.list[0].seq)
    i = 0
    while path[i+1]!=0:
        print('path编号：'+str(path[i]),end='')
        ver = AdjList.findTheEdgeNextVerSeq(path[i],AdjList)
        print(str(ver)+', ',end='')
        result = result+str(ver)
        i+=1
    print('path编号：'+str(path[i]),end='')
    ver = AdjList.findTheEdgeNextVerSeq(path[i],AdjList)
    print(str(ver)+']')
    result = result+str(ver)
    results.append(result)
    print('----------------')

def DFS(start,depth,AdjList,path,visited):
    if start==AdjList.size-1:
        # print('depth is:'+str(depth))
        path[depth]=0   #mark the end of the path
        printPath(path,AdjList)
    else:
        if visited[start]==0:
            # print('start:'+str(start))
            visited[start]=1
            link = AdjList.list[start].link
            # print('link:'+str(link.seq))
            while link!=None:
                path[depth] = link.seq
                # print('path['+str(depth)+']:'+str(path[depth]))
                DFS(link.adjvex,depth+1,AdjList,path,visited)
                link = link.next
                # if link!=None:
                #     print('link:'+str(link.seq))
                # else:
                #     print('link: None')
            visited[start]=0
            return

def iterate_Path(AdjList):
    path = [0]*AdjList.size
    visited = [0]*AdjList.size
    DFS(0,0,AdjList,path,visited)


# if __name__=='__main__':
#     n = input("请输入点个数：")
#     e = input("请输入边个数：")
#     adjList =  Adjlist().createAdjList(int(n))
#     for i in range(0,int(e)):
#         seq=input('请输入第'+str(i+1)+'边序号:')
#         v1=input('请输入第'+str(i+1)+'点序号1:')
#         v2=input('请输入第'+str(i+1)+'点序号2:')
#         seq = int(seq)
#         v1=int(v1)
#         v2=int(v2)
#         adjList.insertEdge(seq,adjList.list[v1],v2)
#         # adjList.insertEdge(seq,adjList.list[v2],v1)
#     iterate_Path(adjList)


    






# h=[0]*10
# h[0]=0
# h[1]=1
# print(h)
# adjlist = Adjlist().createAdjList(3)
# adjlist.insertEdge(1,adjlist.list[0],1)
# adjlist.insertEdge(1,adjlist.list[1],0)
# adjlist.insertEdge(2,adjlist.list[0],2)
# adjlist.insertEdge(2,adjlist.list[2],0)
# edge = adjlist.list[0].link
# while edge!=None:
#     print(str(edge.seq)+'>>')
#     edge = edge.next


# adjList = Adjlist(5)
# adjList.createAdjList(5)


# adjList = Adjlist(5)
# adjList.list = []
# adjList.list.append(Vertex(5))
# print(adjList.list[0].seq)


# for i in range(1, 5):
#     print(i)
# else:
#     print('for循环结束')

