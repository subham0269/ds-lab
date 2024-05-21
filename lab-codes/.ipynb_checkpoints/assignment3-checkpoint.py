# -*- coding: utf-8 -*-
import re
import networkx as nx
import matplotlib.pyplot as plt

import math
from collections import Counter

import nltk
nltk.download("wordnet")
from nltk.corpus import wordnet as wn
from nltk.tokenize import regexp_tokenize
from nltk.corpus import stopwords
stop_words = set(stopwords.words('english'))
WORD = re.compile(r'\w+')


all_hashtag=[]

def remove_urls(text, replacement_text=""):
	url_pattern = re.compile(r'https?://\S+|www\.\S+')
	text_without_urls = url_pattern.sub(replacement_text, text)
	return text_without_urls

def remove_anno(text, replacement_text=""):
    pattern=re.compile(r"@\w+")
    text_without = pattern.sub(replacement_text, text)
    return text_without

def find_hash(text):
    pattern=r"#\w+"
    hashtag = regexp_tokenize(text,pattern)
    #print(hashtag)
    for i in hashtag:
        if i.lower() not in all_hashtag:
            all_hashtag.append(i.lower())
    return text

def remove_digit(text, replacement_text=""):
    pattern=re.compile(r"\d+")
    text_without = pattern.sub(replacement_text, text)
    return text_without

#temp = input("Enter The Name!! ") 
files= open("d:/Teaching/Python/utkd_data.txt",encoding='utf-8').readlines()

count=0
word=[]
line_words=[]
all_words=[]
for line in iter(files):
    if count<20:
            line=line.strip()
            line=line.lower()
            line=remove_urls(line)
            line=remove_anno(line)
            line =find_hash(line)
            line=remove_digit(line)
            
            #print(line)
            
            #line1=line.split(" ")
            #for i in line1:
                #all_words.append(i)

            pattern=r"[a-z|#]\w+"
            node=re.findall(pattern,line)
            #print(node)
            line_list=[]
            #node=line.split(' ')            
            for i in node:
                if i not in stop_words:
                      if len(i) >= 0:
                           all_words.append(i)                   
                           if i[0]!='#':
                            line_list.append(i)
                            if i not in word:
                                word.append(i)
            #print(line_list)
            line_words.append(line_list)
            count=count+1
            
#print(all_words) 
#print(word)        
            
            
print("Total distnct words: "+str(len(word)))
#print(all_words)  
#print(all_hashtag)
print("Total hashtags: "+str(len(all_hashtag)))
chashtag={}
for i in all_hashtag:
    c=1
    for j in range(len(all_words)):
        if i == all_words[j]:
            c=c+1
    chashtag[i]=c
#print(chashtag)


sorted_chashtag={key: val for key, val in sorted(chashtag.items(), key = lambda ele: ele[1],reverse = True)}

#print(sorted_chashtag)
#print(sorted_chashtag.keys())
#print(sorted_chashtag.values())

cnt=0
for i in sorted_chashtag.keys():
     cnt=cnt+1
     if cnt <=3:
          print(str(i)+"=>"+str(sorted_chashtag[i]))


file1 = open('D:/Teaching/Python/demofile.csv', 'w')
s=''
for i in word:
     s=s+i+','
s=s[0:len(s)-1] + '\n'
#print(s)
file1.write(s)

for i in line_words:
    #print(i)
    s=''
    for j in word:
        if j in i:
             s=s + (str(1)+',')
        else:
             s=s + (str(0)+',')
    s=s[0:len(s)-1] + '\n'
    #print(s+"\n \n")
    file1.write(s)
file1.close()

"""
for i in word:
    syns = wn.synsets(i)
    for s in syns:
        for l in s.lemmas():
             print(l.name())
            #if l.name() in word:
                 #print(i+"->"+l.name()) 
    print("=====================")   

"""


#------------------------------------More than 2 word count similarity---------------------------#
def word_sim(words1,words2):
    match=0
    
    len1=len(words1)
    len2=len(words2)

    if len1 < len2:
            for i in words1:
                    if i in words2:
                            match=match+1
    else:
             for i in words2:
                     if i in words1:
                             match=match+1
    return match
#------------------------------------More than 3 word count similarity---------------------------#


#------------------------------------COSINE similarity-------------------------------------------#
def get_cosine(vec1, vec2):
     intersection = set(vec1.keys()) & set(vec2.keys())
     numerator = sum([vec1[x] * vec2[x] for x in intersection])

     sum1 = sum([vec1[x]**2 for x in vec1.keys()])
     sum2 = sum([vec2[x]**2 for x in vec2.keys()])
     denominator = math.sqrt(sum1) * math.sqrt(sum2)

     if not denominator:
        return 0.0
     else:
        return round(float(float(numerator) / denominator),2)

def text_to_vector(text):
     words = WORD.findall(text)
     return Counter(words)
#------------------------------------COSINE similarity-------------------------------------------#



nodes=[]
node_from=[]
node_to=[]
node_weight=[]
index1=0
for i in range(len(line_words)):
    s1=line_words[i]
    l1=' '.join(s1)
    index1=index1+1
    index2=0
    for j in range(len(line_words)):
        index2=index2+1
        if j != i:
            count=0
            cosine=0
 

            s2=line_words[j]
            l2=' '.join(s2)
            count=word_sim(s1,s2)
            if count >= 2:
                v1=text_to_vector(l1)
                v2=text_to_vector(l2)
                
                cosine=get_cosine(v1,v2)

                node_from.append(index1)
                node_to.append(index2)
                node_weight.append(cosine+count)
                #print(str(index1)+'->'+str(index2)+' :: '+ str(cosine))
k=0            
for i in range(0,len(line_words)):
     k=k+1
     nodes.append(k)

tweight=0
egs=0
G1=nx.DiGraph()
#G1.add_nodes_from(nodes)
for i in nodes:
     G1.add_node(i, label=i)


for s in range(0,len(node_from)):
        G1.add_edge(node_from[s],node_to[s],weight=node_weight[s])
        tweight=tweight+node_weight[s]
        egs=egs+1
        
print ('Total Edges:: ' + str(egs))

# Set node positions
pos = nx.spring_layout(G1)

# Draw nodes and labels
nx.draw_networkx_nodes(G1, pos)
nx.draw_networkx_labels(G1, pos, labels=nx.get_node_attributes(G1, 'label'))

# Draw edges with weights
edge_labels = nx.get_edge_attributes(G1, 'weight')
nx.draw_networkx_edge_labels(G1, pos, edge_labels=edge_labels)
nx.draw_networkx_edges(G1, pos)

# Show graph
plt.axis('off')
plt.savefig("filename.png") 
plt.show()