def findX(var,dvar):
    i=1
    while((var*i)%dvar)!=1:
        i=i+1
    return i

n = int(input("NO. of equations "))
m=[]
b=[]
x=[]
divisors=[]
i=0
while i!=n:
    print("Divisior [%(n)s] " % {'n': i},end="")
    d=int(input(''))

    print("Remainder [%(n)s] " % {'n': i},end="")
    r = int(input(''))
    divisors.append(d)
    b.append(r)
    print()
    i=i+1

mul=1
for j in divisors:
    mul=mul*j

i=0
while i!=n:
    temp=mul/divisors[i]
    m.append(temp)
    i=i+1

i=0
while i!=n:
    print('x %',end="")
    print(" %(q)s = %(w)s"% {'q': divisors[i],'w':b[i]})
    i=i+1

i=0
while i!=n:
    var=m[i]%divisors[i]
    print(var)
    temp=findX(var,divisors[i])
    x.append(temp)
    i=i+1

i=0
sum=0
while i!=n:
    sum=sum+b[i]*m[i]*x[i]
    i=i+1

answer=sum%mul
print("According to chinese remainder theorem, X = %(q)s " % {'q': answer})
