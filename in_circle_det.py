def det(l):
    n=len(l)
    if (n>2):
        i=1
        t=0
        sum=0
        while t<=n-1:
            d={}
            t1=1
            while t1<=n-1:
                m=0
                d[t1]=[]
                while m<=n-1:
                    if (m==t):
                        u=0
                    else:
                        d[t1].append(l[t1][m])
                    m+=1
                t1+=1
            l1=[d[x] for x in d]
            sum=sum+i*(l[0][t])*(det(l1))
            i=i*(-1)
            t+=1
        return sum
    else:
        return (l[0][0]*l[1][1]-l[0][1]*l[1][0])

def in_circle(vertex, triangle):
    #get the coordinate of the triangle
    x1 = triangle[0][0]
    y1 = triangle[0][1]
    x2 = triangle[1][0]
    y2 = triangle[1][1]
    x3 = triangle[2][0]
    y3 = triangle[2][1]

    # create the matrix
    A =    [[x1,x2,x3,vertex[0]],
            [y1,y2,y3,vertex[1]],
            [x1**2 +y1**2,x2**2+y2**2,x3**2+y3**2,vertex[0]**2+vertex[1]**2],
            [1,1,1,1]]

    det_value= det(A)
    print 'det_value'
    print det_value

    if  det_value > 0:
        return True
    else:
        return False
