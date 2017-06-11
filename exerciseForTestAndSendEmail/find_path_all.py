from getData_17.5.26 import Adjlist
def find_path_all(begin, finish, file_path):  
    ''''' 
    :param begin: 初始顶点 
    :param finish: 要到达的顶点 
    :param file_path: 要读取文件的路径 
    :return: '''
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
    for end in range(begin,finish):
        for start in range(begin,finish):
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
                    elif itera < 0 or itera<begin:
                        continue
                    elif (end>start and itera > end) or (start>end and itera>start) or itera>finish:
                        break
                    else:
                        line = line.split()
                        if int(line[0])==-1:
                            continue
                        for v2 in line:
                            if (int(v2)<=finish and int(v2)>=begin and itera<=finish and itera>=begin) and \
                            ( (end>start and int(v2)<=end and int(v2)>=start and itera<=end and itera>=start) or \
                                (start>end and int(v2)<=start and int(v2)>=end and itera<=start and itera>=end)):
                                '''通过查找编号点在数组中物理位置插入'''
                                adjList.insertEdge(theGraphEdgeNumber,adjList.list[adjList.findTheVertex(itera,adjList)],adjList.findTheVertex(int(v2),adjList))
                                theGraphEdgeNumber = theGraphEdgeNumber+1
            adjLists.append(adjList)
    
    results = getIsolateResults(adjLists)    
    print('this is results:'+str(len(results)))
    print(results)
    # new_results = multicpu.multi_cpu(getTheNewResults,results,8,1)
    new_results = getTheNewResults(results)
    print('this is the new results:'+str(len(new_results)))
    print(new_results)
    return new_results