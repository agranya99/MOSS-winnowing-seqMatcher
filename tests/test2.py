import math
def dist2(p1,p2):
    d=math.sqrt(((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2))
    return d
def dist3(p1,p2,p3):
    d1=math.sqrt(((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2))
    d2=math.sqrt(((p1[0]-p3[0])**2 + (p1[1]-p3[1])**2))
    d=d1+d2
    return d
def largest_rectangle():
    l1=[]
    l2=[]
    for i in range(n):
        for j in range(i, n):
            for k in range(j,n):
                if points[i][0]==points[j][0] and points[i][1]==points[k][1]:
                    x1=points[k][0]
                    y1=points[j][1]
                    if (x1,y1) in points:
                        d=dist3(points[i], points[j], points[k])
                        l1=[points[i], points[j], points[k], (x1,y1), d]
                        l2.append(l1)
    l2=sorted(l2, key=lambda x:x[-1], reverse=True)
    print(l2[0])
def largest_square():
    l1=[]
    l2=[]
    for i in range(n):
        for j in range(i, n):
            for k in range(j,n):
                if points[i][0]==points[j][0] and points[i][1]==points[k][1] and dist2(points[i], points[j])==dist2(points[i], points[k]):
                    x1=points[k][0]
                    y1=points[j][1]
                    if (x1,y1) in points:
                        d=dist3(points[i], points[j], points[k])
                        l1=[points[i], points[j], points[k], (x1,y1), d]
                        l2.append(l1)
    l2=sorted(l2, key=lambda x:x[-1], reverse=True)
    if l2[0][-1]==0:
        print('No square.')
    else:
        print(l2[0])

n=int(input())
points=[]
for i in range(n):
    x=int(input())
    y=int(input())
    points.append((x,y))
largest_rectangle()
largest_square()
