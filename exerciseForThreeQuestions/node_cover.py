import copy  
import datetime

def find_path_all(curr, end, path):  
    ''''' 
    :param curr: 当前顶点 
    :param end: 要到达的顶点 
    :param path: 当前顶点的一条父路径 
    :return: 
    ''' 
    if curr == end:
        path_tmp = copy.deepcopy(path)  
        path_simple.append(path_tmp)  
        return    
    if not graph.get(curr):  
        return  
    for v in graph[curr]:   
        if v not in path:
            # 造下次递归的父路径  
            path.append(v)  
            find_path_all(v,end,path)
            path.pop() 

print ('输入end以退出\n')
while True:
    file_name = input('输入测试样例：')
    begin = datetime.datetime.now()
    if file_name == 'end':
        break
    # 读txt到字典
    graph = {}
    i = 0
    try:
        with open('test_case/%s' % file_name, 'r') as file:
            for nextNode in [f.strip('[]\n').split(', ') for f in file]:
                if i != 0:
                    graph['%d' % int(i-1)] = nextNode
                i += 1
        print ('样例：%s' %graph)

        # 输出simple path
        path_primes = []
        # for startKey in graph.keys():
        #     for endKey in graph.keys():
        startKey = '0'  # -1    4
        endKey = '6'   #   6    4
        path_simple = [] 
        find_path_all(startKey, endKey, path=[startKey])
        if startKey in graph.get(endKey):
            for i in path_simple:
                i.append(startKey)
        if path_simple != []:
            path_primes += path_simple
            print ("start %s -- end %s: " % (startKey, endKey), path_simple)
    except: 
        print("文件名错误，请重新输入！\n") 