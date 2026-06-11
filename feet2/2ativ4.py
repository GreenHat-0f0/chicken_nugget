x=0
y=int(input("Digite um número: "))
while x!=y and x!=y-1 and x!=y+1:
    print(x)
    if y>x:
        x=x+2
    else:
        x=x-2
print(y)
