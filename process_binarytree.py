"""
this code translate the stanford parser result into birary tree and remove the label.
result after process is as follows:
( ( A person ) ( ( is ( training ( ( his horse ) ( for ( a competition ) ) ) ) ) . ) )

author: Xingwei He
date: 2017.1.11 
"""
import sys

"""
construct tree from string
"""
def parse(treestr,index=0):
  #we use dict save the tree
  t={}
  children={}
  index=index+1
  while treestr[index]!=')':
    if treestr[index]=='(':
      index,t=parse(treestr,index)
      children[len(children)+1]=t
    elif treestr[index]==' ':
      index+=1
      continue
     #leaf node
    else:
      rpos=min(treestr.find(' ',index),treestr.find(')',index))
      leaf=treestr[index:rpos]
      if leaf!='':
        children[len(children)+1]={'value':leaf,'children':{}}
      index=rpos
    
  t={'value':None,'children':children}
  return index+1,t
    
"""
visit the tree in pre order
""" 
def preorder(tree):
  s=[]
  if len(tree['children'])==1:
    s.extend(preorder(tree['children'][1]))
  elif len(tree['children'])==2:
    s.append('(')
    s.extend(preorder(tree['children'][1]))
    s.extend(preorder(tree['children'][2]))
    s.append(')')
  elif tree['children']=={}:
    s.append(tree['value'])
  return s

"""
remove the pos tag
"""  
def removeLabel(line):
  line=line.replace('\n','')
  length=len(line)
  l=[]
  i=0
  while i<length:
    c=line[i]
    if c=='(':
      l.append(c)
      i+=1
      while line[i]!=' ':
        i+=1
      l.append(line[i])
    elif c==')':
      l.append(' )')
    else:
      l.append(c)
    i+=1
  return ''.join(l)        



def process(line):
  line=removeLabel(line)
  line=line.replace('\n','')
  #load tree from input string
  
  _,t=parse(line)
  s=preorder(t)
  return ' '.join(s)

  
if __name__=="__main__":
  for line in sys.stdin:
    line=process(line)
    print line

