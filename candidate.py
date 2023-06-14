l=[["round","triangle","round","purple","yes","yes"],["square","square","square","green","yes","no"],["square","triangle","round","yellow","yes","yes"],["round","triangle","round","green","no","no"],["square","square","round","yellow","yes","yes"]]
for i in l:
    print(i)
print()
print()
print("------- SPECIFIC --------")
print()
h=["Null",]*5
print(h)
x=1
for i in l:
    x+=1
    if(i[-1]=="yes"):
        h=i[:-1]
        print(h)
        break
    print(h)
for i in l[x:]:
    if(i[-1]=="no"):
        print(h)
        continue
    for j in range(len(i[:-1])):
        if(i[j]!=h[j]):
            h[j]="?"
    print(h)
print()
print()
print("------- GENERAL --------")
print()
g=["?",]*5
x=0
for i in l:
    
    if(i[-1]=="yes" and x==0):
        x+=1
        h=i[:-1]
        
    elif(i[-1]=="yes"):
        for j in range(len(i[:-1])):
            if(i[j]!=h[j]):
                h[j]="?"
    else:
        L=[]
        for j in range(len(h)):
            if(h[j]=="?"):
                continue
            elif(h[j]!=i[j]):
                L.append(["?",]*j + [h[j],]+ ["?",]*(5-j-1))
            else:
                h[j]="?"
        g=L[::]
    if(g==[]):
        print(["?",]*5)
        continue
    print(g)
        
        
