#!/usr/local/bin/python
#import pdb
import math
import add_vertex

import numpy as np
import matplotlib
import matplotlib.pyplot as plt

def triangulate(vertex_list):

    #pdb.set_trace()
    tri_list = []

    if len(vertex_list)<3:
        return "Not enough vertex"
    else:
        (xMin, xMax, yMin, yMax) = find_bounding_box(vertex_list)
        super_tri = super_triangle(xMin,xMax,yMin,yMax)
        tri_list.append(super_tri)


        for each in vertex_list:
            temp_list = add_vertex.add_vertex(each,tri_list)
            tri_list = temp_list

        #remove all triangles stem from super triangle
        remove_tri_set= set()
        for tri in tri_list:
            for v in tri:
                if v == super_tri[0] or v == super_tri[1] or v == super_tri[2]:
                    if tri not in remove_tri_set:
                        remove_tri_set.add(tri)

        for item in remove_tri_set:
            tri_list.remove(item)

        return tri_list




def find_bounding_box(vertex_list):
    #sort by x coordinate
    x_sorted = sorted(vertex_list, key = lambda  vertex_list:vertex_list[0])
    xMin = x_sorted[0][0]
    xMax = x_sorted[-1][0]

    #sort by y coordinate
    y_sorted = sorted(vertex_list, key = lambda  vertex_list:vertex_list[1])
    yMin = y_sorted[0][1]
    yMax = y_sorted[-1][1]

    dx = xMax - xMin
    dy = yMax - yMin

    #make the bounding box a bit bigger
    ddx = dx*0.01
    ddy = dx*0.01

    xMin -= ddx
    xMax += ddx

    yMin -= ddx
    yMax += ddx

    return  xMin, xMax, yMin, yMax

def super_triangle(xMin, xMax, yMin, yMax):
    dx = xMax - xMin
    dy = yMax - yMin
    node1 = (int(xMin - dy*math.sqrt(3)/3.0)-1,yMin)
    node2 = (int(xMax + dy*math.sqrt(3)/3.0)+1,yMin)
    node3 = ((xMin + xMax)/2.0, yMax + int(math.sqrt(3)*dx/2)+1)
    super_tri = ((node1,node2,node3))
    return super_tri

def main():
    num =  5

    X = np.random.random(num)
    Y = np.random.random(num)
    fig = plt.figure(figsize=(10,10))
    axes = plt.subplot(1,1,1)
    plt.scatter(X,Y)

    #construct vertex_list[(v0_x,v0_y),(v1_x,v1_y)...]
    v_list = []
    for i in range(0, num):
        v_list.append((X[i],Y[i]))

    #Perform Delaunay Triangulation
    tri_list = triangulate(v_list)

    #Construct line_segments for plotting
    segments = []
    for tri in tri_list:
        line1 = [tri[0],tri[1]]
        line2 = [tri[0],tri[2]]
        line3 = [tri[1],tri[2]]
        segments.append(line1)
        segments.append(line2)
        segments.append(line3)

    #plot
    lines = matplotlib.collections.LineCollection(segments, color='0.75')
    axes.add_collection(lines)
    plt.axis([0,1,0,1])
    plt.show()

    print "Voila!"


if __name__ == "__main__":
    main()
