import networkx as nx
import matplotlib.pyplot as plt

def importDS(path):
    f1 = open(path,'r')
    ds=[]
    for i,line in enumerate(f1):
        if i>0 :
            str1=line.replace('\n','').split(',')
            ds.append(str1)
    """s1 =set()
    d1 = {}   # a dictionary which key is number of PS Id    and value is Card id which used that PS
    for i,line in enumerate(ds):
        l1 = repr(line).replace("'",'').replace(']','').replace('[','').split(',')
        s1.add(l1[2])
    for line in ds:
        l1 = repr(line).replace("'",'').replace(']','').replace('[','').split(',')
        p = int(str(l1[2]).replace("'",''))
        if p in d1.keys():
            d1[p].add(int(str(l1[1]).replace("'", '')))
        else:
            d1[p] = set()
            d1[p].add(int(str(l1[1]).replace("'",'')))

    for k in d1:
        print(str(k)+' : '+str(d1[k]))
    """
    print('===============================================')
    s2 =set()
    d2 = {}   # a dictionary which key is number of card Id    and value is ps id which servved that card
    for i,line in enumerate(ds):
        l2 = repr(line).replace("'",'').replace(']','').replace('[','').split(',')
        s2.add(l2[1])
    for line in ds:
        l2 = repr(line).replace("'",'').replace(']','').replace('[','').split(',')
        p = int(str(l2[1]).replace("'",''))
        if p in d2.keys():
            d2[p].add(int(str(l2[2]).replace("'", '')))
        else:
            d2[p] = set()
            d2[p].add(int(str(l2[2]).replace("'",'')))
    d3={}
    for k in d2:
        if len(d2[k]) > 1:
              d3[k]=d2[k]
    return d3



"""
G=nx.Graph()
G.add_edge(1,2, label=str(122))

H=nx.Graph()
H.add_edge(1,3)
F = nx.compose(G,H)
F.edges()
nx.draw(F)
plt.show(F)
"""


def HCluster(Dict1):
    set1 = set()
    faravaniDict = {}
    for k, v in s2.items():
        temp = str(v).replace('}','').replace('{','').split(',')
        for row in temp:
            set1.add(row)
        print(str(k) + ' : ' + str(v))
    for a in set1:
        for b in set1:
            if str(a).strip()!=str(b).strip() :
                for  k,v in s2.items():
                    if a in str(v) and b in str(v) :
                        if str(a).strip()+'|'+str(b).strip() in faravaniDict.keys() : faravaniDict[str(a).strip()+'|'+str(b).strip()]+=1
                        elif str(b).strip()+'|'+str(a).strip() in faravaniDict.keys() : faravaniDict[str(b).strip()+'|'+str(a).strip()]+=1
                        else: faravaniDict[str(a).strip()+'|'+str(b).strip()]=1
    print('====================')
    max = 0
    maxIndice = ''
    for k,v in faravaniDict.items():
        print(str(k)+ '   = '+str(v))
        if v>max :
            max = v
            maxIndice = k

    print(maxIndice)
    i = maxIndice.index('|')
    max1 = maxIndice[:i]
    max2 = maxIndice[i+1:]
    print(i)
    f={}
    for k,v in faravaniDict.items():
        j= k.index('|')
        ps1=str(k)[:j]
        if ps1==max1 or ps1==max2 : print('('+maxIndice.replace('|','')+')')
        ps1=str(k)[j+1:]
        if str(ps1).strip()==str(max1).strip()  :
            f[str(k).replace(str(max1).strip(),'('+maxIndice.replace('|','*')+')')]=v+faravaniDict[maxIndice]
        elif  str(ps1).strip()==str(max2).strip():
            f[str(k).replace(str(max2).strip(), '(' + maxIndice.replace('|', '*') + ')')] = v + faravaniDict[maxIndice]
        else:
            f[k]=v
    print(']]]]]]]]]]]]]]]]]]]]]]]]]]]]')
    for k,v in faravaniDict.items():
        print(str(k)+ ' = '+str(v))
    #while(len(faravaniDict.keys())!=1):




s2 = importDS('transactiondata.csv')
HCluster(s2)
