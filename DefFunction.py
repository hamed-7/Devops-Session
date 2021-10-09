'''def ecrit():
    a=-1
    while(a<0):
        a=input("donnez number positive a")
    return (a)
def puissance(x,n): 
    if(n==0):
        return(1)
    else:
        x=x*puissance(x,n-1)
        return(x)  
x=ecrit()
y=puissance(x,3)
print(x,y)'''
def saisi():
    n=input("donnez n")
    b=0
    while(b<2)and(b>8):
        b=int(input("donnez a"))
    return (n,b)
print(saisi())
