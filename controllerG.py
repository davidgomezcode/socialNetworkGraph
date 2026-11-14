import modelG
import servicesG
import viewG


def buildGraph(graph): # use case 1: the empty graph gets 12 users with different roles and 21 relations
    users = [
        (1, "David", modelG.VertexRol.student),
        (2, "Sebastián", modelG.VertexRol.student),
        (3, "Carolina", modelG.VertexRol.teacher),
        (4, "Mariana", modelG.VertexRol.graduate),
        (5, "Luna", modelG.VertexRol.student),
        (6, "Alejandro", modelG.VertexRol.teacher),
        (7, "María José", modelG.VertexRol.student),
        (8, "Felipe", modelG.VertexRol.graduate),
        (9, "Aurora", modelG.VertexRol.student),
        (10, "Ricardo", modelG.VertexRol.teacher),
        (11, "Valentina", modelG.VertexRol.graduate),
        (12, "Santiago", modelG.VertexRol.student)
    ]
    for id, name, rol in users:
        code = servicesG.createVertex(graph, id, name, rol)
        viewG.printResult("createVertex", f"id={id}, name={name}, rol={rol.name}", code)

    relations = [ # 1 and 5 follow 4 users, there are cycles (1-3-4-1 and 5-8-5) and 10 and 12 have no followers
        (1, 2), (1, 3), (1, 4), (1, 5),
        (2, 3), (2, 6),
        (3, 4),
        (4, 1),
        (5, 6), (5, 7), (5, 8), (5, 9),
        (6, 7),
        (7, 8),
        (8, 5),
        (9, 11),
        (10, 1), (10, 5), (10, 9),
        (12, 11), (12, 9)
    ]
    for origin, destination in relations:
        code = servicesG.createEdge(graph, origin, destination)
        viewG.printResult("createEdge", f"{origin} follows {destination}", code)

    viewG.printAdjacencyList(graph)


def runTraversals(graph): # use case 2: 3 breadth-first searches from different users and 1 complete depth-first search
    for start in [1, 10, 12]:
        code, visited = servicesG.bfs(graph, start)
        if code == 0:
            viewG.printTraversal(f"Breadth-first search (BFS) from user {start}, visit order:", graph, visited, "Vertexes reached")
        else:
            viewG.printResult("bfs", f"start={start}", code)

    code, discoveryOrder, cycles = servicesG.dfs(graph)
    viewG.printTraversal("Complete depth-first search (DFS), discovery order:", graph, discoveryOrder, "Vertexes discovered")
    viewG.printCycles(cycles)


def runQueries(graph): # use case 3: social queries and reachability
    viewG.printVertexList("Users without followers (in-degree 0):", graph, servicesG.usersWithoutFollowers(graph))

    degree, ids = servicesG.mostInfluential(graph)
    viewG.printDegreeQuery("Most influential users (highest in-degree)", graph, degree, ids)

    degree, ids = servicesG.mostActive(graph)
    viewG.printDegreeQuery("Most active users (highest out-degree)", graph, degree, ids)

    for origin, destination in [(1, 11), (11, 1), (12, 10)]:
        code, reachable = servicesG.canReach(graph, origin, destination)
        viewG.printReachability(origin, destination, code, reachable)


def showChange(graph, operation, description, code): # after each operation the result is printed and, if the graph changed, the new adjacency list too
    viewG.printResult(operation, description, code)
    if code == 0:
        viewG.printAdjacencyList(graph)


def runCrud(graph): # use case 4: add, delete and update, including attempts that must be rejected
    code = servicesG.createVertex(graph, 13, "Mateo", modelG.VertexRol.student)
    showChange(graph, "createVertex", "id=13, name=Mateo, rol=student", code)

    code = servicesG.createVertex(graph, 13, "Mateo", modelG.VertexRol.student) # repeated vertex
    showChange(graph, "createVertex", "id=13, name=Mateo, rol=student", code)

    code = servicesG.createEdge(graph, 13, 5)
    showChange(graph, "createEdge", "13 follows 5", code)

    code = servicesG.createEdge(graph, 13, 5) # repeated edge
    showChange(graph, "createEdge", "13 follows 5", code)

    code = servicesG.createEdge(graph, 13, 13) # a user following itself
    showChange(graph, "createEdge", "13 follows 13", code)

    code = servicesG.deleteEdge(graph, 13, 5)
    showChange(graph, "deleteEdge", "13 stops following 5", code)

    code = servicesG.updateVertex(graph, 2, "Juan Sebastián", modelG.VertexRol.graduate) # name and rol change, the relations stay
    showChange(graph, "updateVertex", "id=2, name=Juan Sebastián, rol=graduate", code)

    code = servicesG.deleteVertex(graph, 5) # the relations that pointed to 5 disappear too
    showChange(graph, "deleteVertex", "id=5", code)

    code = servicesG.deleteVertex(graph, 99) # a vertex that does not exist
    showChange(graph, "deleteVertex", "id=99", code)


def run(): # the only function that main calls: it runs the use cases in order
    graph = modelG.Graph("CampusNet")

    viewG.printTitle("Graph construction")
    buildGraph(graph)

    viewG.printTitle("Traversals")
    runTraversals(graph)

    viewG.printTitle("Social queries")
    runQueries(graph)

    viewG.printTitle("CRUD operations")
    runCrud(graph)
