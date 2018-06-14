def sum_equi(a,b=[]):
    a1=str(a)
    flag=0
    for i in b:
        i1=str(i)
        if len(i1)==len(a1):
            sum1=0
            sum2=0
            for j in a1:
                sum1+=int(j)
            for j in i1:
                sum2+=int(j)
            if sum1==sum2:
                print(i)
                flag=1
    if flag==0:
        print('No sum-equivalent')

n=int(input())
x1=int(input())
x=[]
for i in range(n-1):
    x.append(int(input()))
print(n)
sum_equi(x1,x)
