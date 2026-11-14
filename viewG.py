messages = { # what each return code means, for every operation. The view is the only place that talks to the console
    "createVertex": {
        0: "vertex created",
        1: "rejected, invalid id (it must be an int)",
        2: "rejected, invalid rol (it must be a VertexRol)",
        3: "rejected, invalid name (it must be a text that is not blank)",
        4: "rejected, repeated id (the vertex already exists)"
    },
    "deleteVertex": {
        0: "vertex deleted (the relations that pointed to it were deleted too)",
        1: "rejected, invalid id (it must be an int)",
        2: "rejected, id not found"
    },
    "updateVertex": {
        0: "vertex updated",
        1: "rejected, invalid id (it must be an int)",
        2: "rejected, invalid rol (it must be a VertexRol)",
        3: "rejected, invalid name (it must be a text that is not blank)",
        4: "rejected, id not found"
    },
    "createEdge": {
        0: "relation created",
        1: "rejected, origin and destination must be int",
        2: "rejected, the origin does not exist",
        3: "rejected, the destination does not exist",
        4: "rejected, repeated relation (it already follows that user)",
        5: "rejected, a user cannot follow itself"
    },
    "deleteEdge": {
        0: "relation deleted",
        1: "rejected, origin and destination must be int",
        2: "rejected, the origin does not exist",
        3: "rejected, the destination does not exist",
        4: "rejected, there is no relation between them"
    },
    "bfs": {
        1: "rejected, invalid id (it must be an int)",
        2: "rejected, id not found"
    },
    "canReach": {
        1: "rejected, invalid id (it must be an int)",
        2: "rejected, id not found"
    }
}


def describe(graph, id): # returns the full info of a vertex as text: id, name and rol
    vertex = graph.vertexes[id]
    return f"{vertex.id} {vertex.name} ({vertex.rol.name})"


def printTitle(title): # separates the use cases in the console
    print()
    print("=== " + title + " ===")


def printResult(operation, description, code): # prints what was tried and what happened
    print(f"[{operation}] {description}: {messages[operation][code]}")


def printAdjacencyList(graph): # prints every user followed by the ids of the users it follows
    print("Adjacency list of " + graph.name + ":")
    for origin in graph.edges:
        destinations = []
        for destination in graph.edges[origin]:
            destinations.append(str(destination))
        if len(destinations) == 0: # a user that follows nobody
            text = "-"
        else:
            text = ", ".join(destinations)
        print(f"  {describe(graph, origin)} -> {text}")


def printTraversal(title, graph, ids, countLabel): # prints the order of a traversal with the full info of each vertex and how many there are
    print(title)
    position = 1
    for id in ids:
        print(f"  {position}. {describe(graph, id)}")
        position += 1
    print(f"{countLabel}: {len(ids)}")


def printCycles(cycles): # prints every cycle as a path that comes back to where it started
    if len(cycles) == 0:
        print("Cycles found: none")
        return
    print(f"Cycles found: {len(cycles)}")
    for cycle in cycles:
        path = []
        for id in cycle:
            path.append(str(id))
        print("  " + " -> ".join(path))


def printVertexList(title, graph, ids): # prints a title and the full info of each vertex in the list
    print(title)
    if len(ids) == 0:
        print("  none")
    for id in ids:
        print(f"  {describe(graph, id)}")


def printDegreeQuery(title, graph, degree, ids): # prints a query about the highest degree and the users that have it
    printVertexList(f"{title}, degree {degree}:", graph, ids)


def printReachability(origin, destination, code, reachable): # prints if the origin can arrive to the destination
    if code != 0:
        printResult("canReach", f"{origin} to {destination}", code)
    elif reachable:
        print(f"[canReach] user {origin} can reach user {destination}: yes")
    else:
        print(f"[canReach] user {origin} can reach user {destination}: no")
