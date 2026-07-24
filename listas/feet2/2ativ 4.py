x=0
y=int(input("Digite um número: "))
if y>x:
    while x!=y and x!=y-1:
        print (x)
        x=x+2
elif y<x:
    while x!=y and x!=y+1:
        print (x)
        x=x-2
        
if x==y-1 or x==y+1:
    print (x)
else:
    print(y)
