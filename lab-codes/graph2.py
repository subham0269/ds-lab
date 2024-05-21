from matplotlib import pyplot as plt
f = open("D:/Teaching/Python/dataset.csv", "r")
line_no=0
country=[]
total_case=[]
for x in f:
    if line_no>10:
        line=x.strip('\n')
        line=line.split(',')
        print(line)
        country.append(line[0])
        data=line[1].replace('"','')
        total_case.append(int(data))
    line_no=line_no+1

#print (country)
print (total_case)
plt.bar(country,total_case) 
plt.show() 
