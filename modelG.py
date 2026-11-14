from enum import Enum

class VertexRol(Enum): # these are the only roles that a vertex can have. 
    student = 1
    teacher = 2
    graduate = 3


class Vertex: #Vertex that has id, name and rol
    def __init__(self, id, name, rol):
        self.id = id
        self.name = name
        self.rol = rol
    
    def __repr__(self):
        return f"Vertex(id={self.id}, name={self.name}, rol={self.rol.name})"


# The Edge class stays here for form's sake (the assignment lists it in the model), but it is commented
# because it is not doing any function: the adjacency list in Graph.edges stores plain ids, so no Edge object is ever created.
# class Edge: # the edge is the connector between vertexes. It has an origin (vertex from it starts) and a destination (vertex to which it arrives) 
#     def __init__(self, origin, destination):
#         self.origin = origin
#         self.destination = destination


class Graph: # the graph is the meta-structure that holds everything. It contains both the vertexes and the connection between them
    def __init__(self, name):
        self.name = name
        self.vertexes = {} # Here we add all the vertexes of the graph
        self.edges = {} # Adjacency list.Key is the id of origin and the values in the list are the ids of the destinations
