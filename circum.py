import numpy as np
import math

epsilon = 0.000000001

def circumcircle(P1,P2,P3):
    '''
    Adapted from:
    http://local.wasp.uwa.edu.au/~pbourke/geometry/circlefrom3/Circle.cpp
    '''
    delta_a = P2 - P1
    delta_b = P3 - P2
    #simple case: Very simple Right Triangle
    if np.abs(delta_a[0]) <= epsilon and np.abs(delta_b[1]) <= epsilon:
        center_x = 0.5*(P2[0] + P3[0])
        center_y = 0.5*(P1[1] + P2[1])
    else:
        aSlope = delta_a[1]/delta_a[0]
        bSlope = delta_b[1]/delta_b[0]
        if np.abs(aSlope-bSlope) <= 0.000000001:
            return None
        center_x= (aSlope*bSlope*(P1[1] - P3[1]) + bSlope*(P1[0] + P2 [0]) \
                        - aSlope*(P2[0]+P3[0]) )/(2* (bSlope-aSlope) )
        print center_x
        center_y = -1*(center_x - (P1[0]+P2[0])/2)/aSlope +  (P1[1]+P2[1])/2;
    return center_x, center_y

def circumcircle(tri):
    x0 = tri[0][0]
    y0 = tri[0][1]

    x1 = tri[1][0]
    y1 = tri[1][1]

    x2 = tri[2][0]
    y2 = tri[2][1]

    y10 = y1 - y0
    y21 = y2 - y1

    b21zero  = bool(np.abs(y21) <= epsilon)
    b10zero  = bool(np.abs(y10) <= epsilon)

    if b10zero:
        if b21zero:
            #all three vertices are on one horizotal line
            center_x = (max(x0,x1,x2)+min(x0,x1,x2))*0.5
            center_y = y0
        else:
            #v[0] and v[1] are on one horizontal line
            m1 = -(x2 -x1)/y21

            mx1 = (x1+x2)*0.5
            my1 = (y1+y2)*0.5

            center_x = (x0+x1)*0.5
            center_y = m1*(center_x-mx1) + my1
    elif b21zero:
        m0 = -(x1-x0)/y10

        mx0 = (x0+x1)*0.5
        my0 = (y0+y1)*0.5

        center_x = (x1+x2)*0.5
        center_y = m0*(center_x-mx0) + my0

    else:

        m0 = -(x1-x0)/y10
        m1 = -(x2 -x1)/y21

        mx0 = (x0+x1)*0.5
        my0 = (y0+y1)*0.5

        mx1 = (x1+x2)*0.5
        my1 = (y1+y2)*0.5

        center_x = (m0*mx0 - m1*mx1 + my1 - my0)/(m0 - m1)
        center_y = m0*(center_x - mx0) + my0

    dx = x0 - center_x
    dy = y0 - center_y

    radius = math.sqrt(dx**2 + dy**2)

    return center_x, center_y,radius



#def in_circle(tri,vertex):
#    P0 = np.array([tri[0][0],tri[0][1]])
#    P1 = np.array([tri[1][0],tri[1][1]])
#    P2 = np.array([tri[2][0],tri[2][1]])
#
#    V  = np.array([vertex[0],vertex[1]])
#
#
#    (center_x, center_y) = circumcircle(P0,P1,P2)
#    C = np.array([center_x, center_y])
#
#    v_distance = np.dot(V-C, V-C)
#    radius = np.dot(P0-C, P0-C)
#
#    print 'v_distance'
#    print v_distance
#    print 'radius'
#    print radius
#    if v_distance < radius:
#        return True
#    else:
#        return False

def in_circle(tri, vertex):
    (c_x, c_y, r) = circumcircle(tri)
    v_distance = math.sqrt((vertex[0] - c_x)**2 + (vertex[1] - c_y)**2)

    if v_distance < r:
        return True
    else:
        return False


def main():
    tri = ((5,-0.04),(-5,-0.04),(0,8.04))
    vertex = (2,0)
    print circumcircle(tri)
    print in_circle(tri, vertex)


if __name__=="__main__":
    main()


