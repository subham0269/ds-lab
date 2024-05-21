import re
def remove_urls(text, replacement_text=""):
	url_pattern = re.compile(r'https?://\S+|www\.\S+')
	text_without_urls = url_pattern.sub(replacement_text, text)
	return text_without_urls

def remove_anno_hash(text, replacement_text=""):
    pattern=re.compile(r"[@\#]\w+")
    text_without = pattern.sub(replacement_text, text)
    return text_without

def remove_digit(text, replacement_text=""):
    pattern=re.compile(r"\d+")
    text_without = pattern.sub(replacement_text, text)
    return text_without

temp = input("Enter The Name!! ") 
files= open("c:/Users/SNU/Downloads/"+temp,encoding='utf-8').readlines()
count=0
word=[]
for line in iter(files):
    if count<20:
            line=line.strip()
            line=remove_urls(line)
            line=remove_anno_hash(line)
            line=remove_digit(line)
            
            #print(line)
            pattern=r"\w+"
            node=re.findall(pattern,line)
            stopwords=[x for x in node if x not in a]
            print(stopwords)

            #node=line.split(' ')            
            for i in node:
                if i.lower() not in word:
                    word.append(i.lower())
            count=count+1
print(word)  


