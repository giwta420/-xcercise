maxwords=[];word="";
with open("file2.txt") as fileobj:
    for line in fileobj:  
       for ch in line:                              #dhmiourgia listas
            if ch!=" " and ch!="\n":                #me thn prosthikh twn leksewn
               word+=ch                             #pu phrame apo to arxeio
            else:
                maxwords.append(word)
                word=""
fileobj.close()

N=len(maxwords)
for i in range(N):
    for j in range(N-1,-1,-1):
        if maxwords[j]>maxwords[j-1]:                                   #eyresh megalyterwn leksewn
            maxwords[j],maxwords[j-1]=maxwords[j-1],maxwords[j]         #topothetwntas ta stoixeia se fthinusa seira

for i in range(N):
    while N>5:
        maxwords.pop()                                                  #afairesh twn ypoloipwn mikroterwn leksewn
                                                                        #dioti xreiazomaste mono tis 5 megalyteres
lista=[];
for i in range(N):
    leksh=maxwords[i]
    lista=list(leksh)
    M=len(lista)
    for k in range(M):
        if lista[k]=='a':
            lista.remove('a')
                    
        elif lista[k]=='e':
            lista.remove('e')            
                                                                        #afairesh twn fwnhentwn apo thn lista     
        elif lista[k]=='i':
            lista.remove('i')            
            
        elif lista[k]=='o':
            lista.remove('o')        
            
        elif lista[k]=='u':
            lista.remove('u')



print(maxwords[::-1])                                                   #ektypwshs ths listas anapoda xwris ta fwnhenta



