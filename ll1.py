non_terminal=[]
terminal=[]
n=int(input("enter no of non terminals:"))
m=int(input("enter no of terminals:"))
for i in range(n):
    A=input("enter non terminal:")
    non_terminal.append(A)
for i in range(m):
    a=input("enter teminal:")
    terminal.append(a)
#print(non_terminal)
#print(terminal)
gra=[]
no=int(input("enter number of production:"))
for i in range (no):
    pr=input("enter production:")
    gra.append(pr)

#print(gra)
first=[]
follow=[]
for t in non_terminal:
    
    print("first of",t)
    n1=int(input("enter no of first"))
    for i in range (n1):
         print("enter first of",t)
         fir=input()
         first.append(fir)
    print("follow of",t)
    n2=int(input("enter no of follow"))
    for i in range(n2):
        print("enter follow of",t)
        fol=input()
        follow.append(fol)
#print(first)
#print(follow)
table=[]
for g in gra:
    for f in first:
            if f in terminal:
                table.append(g)
                break
for g1 in gra:
    for g2 in follow:
        if "#" in first:
            table.append(g1)
            break
print(table)
            
    
