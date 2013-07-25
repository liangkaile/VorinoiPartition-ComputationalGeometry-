import math
import circum
#import in_circle_det

def add_vertex(vertex, triangle_list):
    edge_buffer = []
    triangle_affected = set()

    #get all affected triangles and edges
    for tri in triangle_list:
        if circum.in_circle(tri,vertex):
            if tri not in triangle_affected:
                triangle_affected.add(tri)

    #remove the affected triangles from triangle_list
    #rember their edges
    for item in triangle_affected:
        edge_buffer.append((item[0], item[1]))
        edge_buffer.append((item[0], item[2]))
        edge_buffer.append((item[1], item[2]))
        triangle_list.remove(item)


    #remove all double edges from edge buffer
    edge_buffer = remove_double_edge(edge_buffer)

    #triangulate the affected area
    new_triangles = triangulating(edge_buffer, vertex)


    triangle_list = triangle_list + new_triangles
    return triangle_list




def remove_double_edge(edge_buffer):
    temp = set()
    for e in edge_buffer:
        if edge_buffer.count(e) == 1:
            temp.add(e)
    return temp


def triangulating(edge_buffer,vertex):
    new_triangles = []
    for e in edge_buffer:
        new_triangles.append((e[0],e[1],vertex))
    return new_triangles

def main():
    triangle = ((0,2),(0,0),(2,0))

    tri_list = [((1,1),(1,0),(0,2)),((0,-2),(1,0),(0,2)),((0,-2),(-1,0),(0,2)),((-7,2),(-1,0),(0,2))]
    vertex = (0.5,0.5)


    print circum.in_circle(triangle,vertex )
    print  add_vertex(vertex,tri_list)

if __name__ == "__main__":
    main()

