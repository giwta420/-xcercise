lista=[];word="";
fin=open("file1.txt","r")
keimeno=fin.read()
for letter in keimeno:
   if letter!=" " and letter!="\n":
       word+=letter
   else:
       lista.append(word)
       word=""
print("h lista einai:",lista)


N=len(lista)
for i in range(N):
    if len(lista[i])>3:
        leksh=lista[i]
        leksh+=leksh[0]
        leksh+="ay"
        leksh=leksh[1 : : ]
        lista[i]=leksh
print("h nea lista einai:",lista)
