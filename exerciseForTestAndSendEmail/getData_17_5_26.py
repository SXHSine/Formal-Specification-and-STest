import unittest
import unittestCase

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
                # print('findTheVertex:'+str(i))
                return i
        return -1
    
    def findTheEdgeNextVerSeq(self,edgeSeq,adjList):
        for i in range(0,len(adjList.list)):
            rear = adjList.list[i].link
            while rear!=None:
                if rear.seq==edgeSeq:
                    # print('findTheEdgeNextVerSeq:  '+str(adjList.list[rear.adjvex].seq))
                    return adjList.list[rear.adjvex].seq
                rear = rear.next
        return -1

class getData_17_5_26:
    # results=[]
    def printPath(path,AdjList,results):
        result = []
        result.append(AdjList.list[0].seq)
        i = 0
        while path[i+1]!=0:
            ver = AdjList.findTheEdgeNextVerSeq(path[i],AdjList)
            result.append(ver)
            i+=1
        ver = AdjList.findTheEdgeNextVerSeq(path[i],AdjList)
        result.append(ver)
        results.append(result)

    def DFS(start,depth,AdjList,path,visited,results):
        if start==AdjList.size-1:
            # print('depth is:'+str(depth))
            path[depth]=0   #mark the end of the path
            getData_17_5_26.printPath(path,AdjList,results)
        else:
            if visited[start]==0:
                visited[start]=1
                link = AdjList.list[start].link
                while link!=None:
                    path[depth] = link.seq
                    getData_17_5_26.DFS(link.adjvex,depth+1,AdjList,path,visited,results)
                    link = link.next
                visited[start]=0
                return

    def iterate_Path(AdjList,results):
        path = [0]*AdjList.size
        visited = [0]*AdjList.size
        getData_17_5_26.DFS(0,0,AdjList,path,visited,results)
        return results

    # def getDuplicate(s):  
    #     s = list(s)
    #     s.sort()
    #     for i in s:  
    #         while s.count(i) > 1:  
    #             return False  
    #     return True  
    def getDuplicate(s):
        '''方法1'''
        # s_new = list(set(s))
        # if s_new==s:
        #     return True
        # return False
        '''方法2'''
        if len(s)==len(set(s)):
            return True
        return False

    def listToStr(result):
        s=''
        for i in result:
            s = s+str(i)+' '
        return s

    def isIncluded(included,include):
        if included in include:
            return True
        return False

    # def isIncluded(included,include):
    #     i = 0
    #     for c in included:
    #         if c != include[i]:
    #             return False
    #         i = i+1 
    #     return True

    def deleteDupicate(results):
        new_results = []
        [new_results.append(i) for i in results if not i in new_results]
        return new_results

    def getAdjLists(file_path):
        file = open(file_path)
        adjLists = []
        '''注意文档中有一行空行'''
        itera=-4            
        line = file.readline()
        line = file.readline()
        line = line.split()
        pointNum = len(line)
        file.close()        
        for end in range(0,pointNum):
            for start in range(0,pointNum):
                if start==end:
                    continue
                file = open(file_path)
                itera=-4
                theGraphEdgeNumber = 0
                while 1:
                    line = file.readline()
                    if not line:
                        break
                    elif line[0]=='#':
                        continue
                    else:
                        itera = itera+1
                        if itera == -3:
                            ls = []
                            if end > start:
                                for i in range(start,end+1):
                                    ls.append(i)
                            else:
                                '''倒序插入，如物理地址0，编号4'''
                                for i in range(end,start+1)[::-1]:
                                    ls.append(i)
                            adjList = Adjlist().createAdjList(abs(end-start)+1,ls)
                        elif itera < 0 or (end<start and itera<end) or (start<end and itera<start):
                            continue
                        elif (end>start and itera > end) or (start>end and itera>start):
                            break
                        else:
                            line = line.split()
                            if int(line[0])==-1:
                                continue
                            for v2 in line:
                                if (end>start and int(v2)<=end and int(v2)>=start and itera<=end and itera>=start) or \
                                    (start>end and int(v2)<=start and int(v2)>=end and itera<=start and itera>=end):
                                    '''通过查找编号点在数组中物理位置插入'''
                                    adjList.insertEdge(theGraphEdgeNumber,adjList.list[adjList.findTheVertex(itera,adjList)],adjList.findTheVertex(int(v2),adjList))
                                    theGraphEdgeNumber = theGraphEdgeNumber+1
                adjLists.append(adjList)
        return adjLists

    def getIsolateResults(adjLists):
        results = []
        for adjList in adjLists:
            getData_17_5_26.iterate_Path(adjList,results)
        return results

    def getTheNewResults(results):
        length_results = 0
        while length_results!=len(results):
            length_results = len(results)
            '''连接加入新元素'''
            length = len(results)
            for r_1 in range(0,length):
                for r_2 in range(0,length):
                    if r_1==r_2:
                        continue
                    s1 = results[r_1]
                    s2 = results[r_2]
                    len1 = len(s1)
                    len2 = len(s2)
                    if s1[len1-1] == s2[0]:
                        results.append(s1[0:len1-1]+s2)
            # print('连接加入新元素后：')
            # print(results)
            '''分析新元素后，删除元素中有环路的元素（除首尾）'''
            length = len(results)
            for r in range(0,length):
                s = results[r]
                s_1 = s[0:len(s)-1]
                s_2 = s[1:len(s)]
                if getData_17_5_26.getDuplicate(s_1)==False or getData_17_5_26.getDuplicate(s_2)==False:
                    results[r] = ''
            for i in range(0,len(results))[::-1]:
                if results[i]=='':
                    results.pop(i)
            # print('删除元素中有环路的元素后：')
            # print(results)
            '''删除重复数据'''
            results = getData_17_5_26.deleteDupicate(results)
            # print('删除重复数据后：')
            # print(results)
        '''最后，比对，删除包含'''
        for r_1 in range(1,len(results)):
            for r_2 in range(0,r_1):
                s1 = getData_17_5_26.listToStr(results[r_1]) 
                s2 = getData_17_5_26.listToStr(results[r_2]) 
                if len(s1)<len(s2) and getData_17_5_26.isIncluded(s1,s2):
                    results[r_1]=''
                elif len(s2)<len(s1) and getData_17_5_26.isIncluded(s2,s1):
                    results[r_2]=''
        for i in range(0,len(results))[::-1]:
            if results[i]=='':
                results.pop(i)
        results = sorted(results, key=lambda a: (len(a), a))#???
        # print('\n this is the new results:'+str(len(results)))
        # print(results)
        return results

    # def f1(results):
    #     for r_1 in range(0,len(results)):
    #         for r_2 in range(0,len(results)):
    #             if r_1==r_2:
    #                 continue
    #             else:
    #                 s1 = ''
    #                 s2 = ''
    #                 for i in results[r_1]:
    #                     s1 = s1+str(i)+' '
    #                 for i in results[r_2]:
    #                     s2 = s2+str(i)+' '
    #                 if s2 in s1:
    #                     results[r_2] = ''
    # def f2(results):
    #     for r_1 in range(1,len(results)):
    #         for r_2 in range(0,r_1):
    #             s1 = listToStr(results[r_1]) 
    #             s2 = listToStr(results[r_2]) 
    #             if len(s1)<len(s2) and isIncluded(s1,s2):
    #                 results[r_1]=''
    #             elif len(s2)<len(s1) and isIncluded(s2,s1):
    #                 results[r_2]=''        

    def getTheLastResults(file_path):
        adjLists = getData_17_5_26.getAdjLists(file_path)
        number = 0
        results = getData_17_5_26.getIsolateResults(adjLists)    
        # print('this is results:'+str(len(results)))
        # print(results)
        # new_results = multicpu.multi_cpu(getTheNewResults,results,8,1)
        new_results = getData_17_5_26.getTheNewResults(results)
        # print('this is the new results:'+str(len(new_results)))
        # print(new_results)
        return new_results

    def getBeginToFinishAdjs(begin, finish, file_path):
        if begin>finish:
            a = begin
            begin = finish
            finish = a
        file = open(file_path)
        adjLists = []
        '''注意文档中有一行空行'''
        itera=-4            
        line = file.readline()
        line = file.readline()
        line = line.split()
        pointNum = len(line)
        file.close()        
        for end in range(begin,finish+1):
            for start in range(begin,finish+1):
                if start==end:
                    continue
                # print('here is new gra:')
                file = open(file_path)
                itera=-4
                theGraphEdgeNumber = 0
                while 1:
                    line = file.readline()
                    if not line:
                        break
                    elif line[0]=='#':
                        continue
                    else:
                        itera = itera+1
                        if itera == -3:
                            ls = []
                            if end > start:
                                for i in range(start,end+1):
                                    ls.append(i)
                            else:
                                '''倒序插入，如物理地址0，编号4'''
                                for i in range(end,start+1)[::-1]:
                                    ls.append(i)
                            adjList = Adjlist().createAdjList(abs(end-start)+1,ls)
                        elif itera < 0 or itera<begin:
                            continue
                        elif (end>start and itera > end) or (start>end and itera>start) or itera>finish:
                            break
                        else:
                            line = line.split()
                            if int(line[0])==-1:
                                continue
                            # print('--loop')
                            for v2 in line:
                                if (int(v2)<=finish and int(v2)>=begin and itera<=finish and itera>=begin) and \
                                ( (end>start and int(v2)<=end and int(v2)>=start and itera<=end and itera>=start) or \
                                    (start>end and int(v2)<=start and int(v2)>=end and itera<=start and itera>=end)):
                                    '''通过查找编号点在数组中物理位置插入'''
                                    adjList.insertEdge(theGraphEdgeNumber,adjList.list[adjList.findTheVertex(itera,adjList)],adjList.findTheVertex(int(v2),adjList))
                                    # print(str(itera)+'---->'+str(v2))
                                    theGraphEdgeNumber = theGraphEdgeNumber+1
                adjLists.append(adjList)
        return adjLists

    def isTheParaRight(begin, finish, file_path):
        '''验证输入是否有误'''
        if begin<0 or finish<0 :
            '''起点或终点有误'''
            return 0
        try:
            file = open(file_path)
        except:
            '''文件路径有误'''
            return 1
        line = file.readline()
        line = file.readline()
        line = line.split()
        pointNum = len(line)
        if begin>pointNum-1 or finish>pointNum-1:
            '''起点或终点有误'''
            return 0
        '''正常'''
        return 2
    def getTheChoosePaths(new_results,compare_re):
        for iterInNew_Re in range(0,len(new_results))[::-1]:
            for s_1  in range(0,len(compare_re)):
                if compare_re[s_1] in new_results[iterInNew_Re]:
                    compare_re[s_1] = ''
            compare_re = list(set(compare_re))
            if  len(compare_re)==1:
                print('here is all of the paths to cover the choosen points:')
                print(new_results[iterInNew_Re:])
                return 1
        print('无法获取覆盖所以指定点的路径')
        return -1

    def find_path_all(begin, finish, file_path):  
        ''''' 
        :param begin: 初始顶点 
        :param finish: 要到达的顶点 
        :param file_path: 要读取文件的路径 
        :return: '''
        isRight = getData_17_5_26.isTheParaRight(begin, finish, file_path)
        if isRight==0:
            print('起点或终点有误')
            return
        elif isRight==1:
            print('文件路径有误')
            return
        adjLists = getData_17_5_26.getBeginToFinishAdjs(begin, finish, file_path)
        results = getData_17_5_26.getIsolateResults(adjLists)    
        print('this is the results of the choosen points:'+str(len(results)))
        print(results)
        # new_results = multicpu.multi_cpu(getTheNewResults,results,8,1)
        new_results = getData_17_5_26.getTheNewResults(results)
        if begin>finish:
            compare_re = [i for i in range(finish,begin+1)]
        else:
            compare_re = [i for i in range(begin,finish+1)]
        getData_17_5_26.getTheChoosePaths(new_results,compare_re)

        # print('this is the new results:'+str(len(new_results)))
        # print(new_results)
        # return new_results


if __name__=='__main__':

    file_path = 'D:\\code\\python\\FormalSAST\\shhe_result\\testcase2'
    answer_path = 'D:\\code\\python\\FormalSAST\\shhe_result\\anwser\\anwser2'
    '''Question1'''
    new_results = getData_17_5_26.getTheLastResults(file_path)
    print('this is the new results:'+str(len(new_results)))
    print(new_results)
    '''Question2'''
    getData_17_5_26.find_path_all(4,0,file_path)
    '''Question3'''
    unittestCase.testUnit(new_results,answer_path)
    





    # from timeit import Timer
    # t1 = Timer('f1([[0, 1], [3, 1], [4, 1], [3, 2], [0, 1, 3], [1, 3], [2, 3], [0, 4]])','from __main__ import f1')
    # t2 = Timer('f2([[0, 1], [3, 1], [4, 1], [3, 2], [0, 1, 3], [1, 3], [2, 3], [0, 4]])','from __main__ import f2')
    # print(t1.timeit(1000))
    # print (t2.timeit(1000))
    # print (t1.repeat(3,1000))
    # print (t2.repeat(3,1000))