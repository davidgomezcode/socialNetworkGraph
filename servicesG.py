import modelG
from collections import deque


def createVertex(graph, id, name, rol): #returns 0 for vertex created, 1 for an invalid id, 2 for an invalid rol, 3 for an invalid name, 4 for repeated id (existing vertex)
    
    if not isinstance(id, int):#id validation, it must be an int
        return 1
    if not isinstance(rol, modelG.VertexRol): #rol validation with enumerate
        return 2
    if not isinstance(name, str) or name.strip() == "": #name validation, it must be a text that is not blank
        return 3
    if id in graph.vertexes: # If the id already exists in the dict as a key then it is rejected
        return 4
    
    newVertex = modelG.Vertex(id, name.strip(), rol)
    
    graph.vertexes[id] = newVertex
    graph.edges[id] = [] # a new vertex follows nobody yet, but it needs its own entry in the adjacency list
    return 0


def deleteVertex(graph, id): #returns 0 for deleted vertex, 1 for an invalid id, 2 for id not found
    if not isinstance(id, int):# id validation, it must be an int
        return 1
    if id not in graph.vertexes: # If the id is not in the graph, there is nothing to delete
        return 2       
    for origin in graph.edges: # the other vertexes may be following the deleted one, so every list is checked
        if id in graph.edges[origin]:
            graph.edges[origin].remove(id)  
    
    graph.edges.pop(id) #we eliminate all the edges from the deleted vertex
    graph.vertexes.pop(id) #we eliminate the vertex from the graph
    return 0


def updateVertex(graph, id, name, rol): #returns 0 for vertex updated, 1 for an invalid id, 2 for an invalid rol, 3 for an invalid name, 4 for nonexisting vertex (no id in vertexes)
    
    if not isinstance(id, int):#id validation, it must be an int
        return 1
    if not isinstance(rol, modelG.VertexRol): #rol validation with enumerate
        return 2
    if not isinstance(name, str) or name.strip() == "": #name validation, it must be a text that is not blank
        return 3
    if id not in graph.vertexes: # If the id is not in the graph, there is nothing to update
        return 4
    
    updatedVertex = modelG.Vertex(id, name.strip(), rol)
    
    graph.vertexes[id] = updatedVertex # the edges are not touched, the id is the same so the relations stay
    return 0
               
             
def createEdge(graph, origin, destination): #returns 0 for edge created, 1 for not using int for origin and destination, 2 for non existing origin, 3 for non existing destination, 4 for repeated edge (destination already followed), 5 for a user following itself 
    if not isinstance(origin, int) or not isinstance(destination, int):
        return 1
    if origin == destination: # a user cannot follow itself
        return 5
    if origin not in graph.edges: #if origin is not in the edges, it means it does not exist yet. There cannot be an edge from a non existing vertex
        return 2
    elif destination not in graph.edges:#if destination is not in the edges, it means it does not exist yet. There cannot be an edge to a non existing vertex
        return 3    
    elif destination in graph.edges[origin]: # if the vertex exists but that destination is already there, it cannot be repeated
        return 4
    else:
        graph.edges[origin].append(destination)
        return 0


def deleteEdge(graph, origin, destination): #returns 0 for edge deleted, 1 for not using int for origin and destination, 2 for non existing origin, 3 for non existing destination, 4 for no edge between them 
    
    if not isinstance(origin, int) or not isinstance(destination, int):
        return 1
    if origin not in graph.edges: #if origin is not in the edges, it means it does not exist yet. There cannot be an edge from a non existing vertex
        return 2
    elif destination not in graph.edges:#if destination is not in the edges, it means it does not exist yet. There cannot be an edge to a non existing vertex
        return 3    
    elif destination not in graph.edges[origin]: # if both origin and destination exists, but there is no edge between them, there is nothing to delete
        return 4
    else:
        graph.edges[origin].remove(destination)
        return 0


def bfs(graph, start): # returns (0, visit order) if ok, (1, []) for an invalid id, (2, []) for a non existing vertex
    if not isinstance(start, int):  # the id must be an int, like in the rest of the functions
        return 1, []
    if start not in graph.vertexes:  # without an existing vertex there is nowhere to start
        return 2, []

    visited = []  # vertices in the order they are visited
    discovered = {start}  # vertices already queued at some point, so a cycle cannot loop forever
    queue = deque([start])  # vertices waiting to be visited

    while queue:  # until there is nothing left to explore
        current = queue.popleft()  # take the one that has been waiting the longest
        visited.append(current)  # record it as visited
        for neighbor in graph.edges[current]:  # every vertex that current follows
            if neighbor not in discovered:  # only the ones not discovered before
                discovered.add(neighbor)  # marked when queued, so it cannot be queued twice
                queue.append(neighbor)  # it will be visited after the ones already waiting

    return 0, visited  # the quantity reached is len(visited)


def dfs(graph): # returns (0, discovery order, cycles found). It is complete: it restarts from every vertex not reached yet
    discoveryOrder = []  # vertices in the order they are reached for the first time
    visited = set()  # vertices already reached, so nothing is explored twice
    path = []  # vertices of the current branch, from where it started down to the current vertex
    cycles = []  # every cycle found, as a list of ids that starts and ends with the same vertex

    def explore(current):
        visited.add(current)  # marked on arrival
        discoveryOrder.append(current)  # this is the order of discovery
        path.append(current)  # current joins the branch being explored
        for neighbor in graph.edges[current]:  # every vertex that current follows
            if neighbor not in visited:  # new vertex: go down into it before looking at the next neighbor
                explore(neighbor)
            elif neighbor in path:  # it is reached again while still in the current branch: that is a cycle
                cycles.append(path[path.index(neighbor):] + [neighbor])  # the branch from neighbor to current, closed with neighbor
        path.pop()  # current is finished, so it leaves the branch

    for vertex in graph.vertexes:  # every vertex, in case some were not reached from the previous ones
        if vertex not in visited:
            explore(vertex)

    return 0, discoveryOrder, cycles


def inDegrees(graph): # returns a dict with the id of each vertex and how many users follow it (in-degree)
    degrees = {}
    for id in graph.vertexes: # everybody starts at 0, so the vertexes that nobody follows are also in the dict
        degrees[id] = 0
    for origin in graph.edges:
        for destination in graph.edges[origin]: # every time an id appears as a destination, it has one more follower
            degrees[destination] += 1
    return degrees


def outDegrees(graph): # returns a dict with the id of each vertex and how many users it follows (out-degree)
    degrees = {}
    for origin in graph.edges:
        degrees[origin] = len(graph.edges[origin]) # the size of its list is the quantity of users it follows
    return degrees


def highestDegree(degrees): # returns (highest degree, list of ids that have it). An empty dict returns (0, [])
    if len(degrees) == 0:
        return 0, []
    highest = max(degrees.values())
    ids = []
    for id in degrees: # there can be a tie, so every id with the highest degree is kept
        if degrees[id] == highest:
            ids.append(id)
    return highest, ids


def usersWithoutFollowers(graph): # returns the list of ids with in-degree 0
    degrees = inDegrees(graph)
    ids = []
    for id in degrees:
        if degrees[id] == 0:
            ids.append(id)
    return ids


def mostInfluential(graph): # returns (highest in-degree, list of ids that have it)
    return highestDegree(inDegrees(graph))


def mostActive(graph): # returns (highest out-degree, list of ids that have it)
    return highestDegree(outDegrees(graph))


def canReach(graph, origin, destination): # returns (0, True) if origin can reach destination, (0, False) if not, (1, False) for an invalid id, (2, False) for a non existing vertex
    if not isinstance(destination, int): # the origin is validated by the bfs
        return 1, False
    if destination not in graph.vertexes:
        return 2, False
    code, visited = bfs(graph, origin) # everything that origin can reach is in the visit order of the bfs
    if code != 0:
        return code, False
    return 0, destination in visited
