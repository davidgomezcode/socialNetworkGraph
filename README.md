# CampusNet – Directed graphs (MVC in Python)

Collaborative Activity II, Programación III – Universidad de Manizales.

Simulation of an academic social network using a directed graph: each vertex is a user (id, name and rol: student, teacher or graduate) and each directed edge A → B means that A follows B.

## Team members

- David Gómez Villegas (individual work)

## Roles and responsibilities

Individual work: David Gómez Villegas developed every layer.

| File             | Layer               | Responsibility                                                                                   |
| ---------------- | ------------------- | ------------------------------------------------------------------------------------------------ |
| `modelG.py`      | Model               | `Vertex` and `Graph` classes and the `VertexRol` enum. The adjacency list lives in `Graph.edges` |
| `servicesG.py`   | Model (graph logic) | Create, delete and update vertexes; create and delete edges; BFS, DFS and social queries         |
| `viewG.py`       | View                | All the console printing                                                                         |
| `controllerG.py` | Controller          | Sequence of use cases and communication between layers                                           |
| `main.py`        | Entry point         | Only calls the Controller                                                                        |

## How to run

Requirements: Python 3. No external libraries are used.

```
py main.py
```

(On Linux or macOS: `python3 main.py`.)

## Design decisions

- Unique identifier: `int`.
- Duplicates are forbidden: a vertex with an existing id and a repeated edge are both rejected.
- The name must be a text that is not blank.
- A user cannot follow itself.
- The adjacency list stores the ids of the destinations (`Dictionary<int, List<int>>`), as the assignment recommends. Since an edge is just an id inside the origin’s list, an Edge object would add nothing, so the class is kept commented out in modelG.py.
- The services never print: they return codes and the View translates them into messages.
- Deleting a user also deletes the relations that pointed to it.

## What the execution shows

1. Graph construction: 12 users with varied roles and 21 relations (2 users with out-degree 4, directed cycles and 2 users without followers).
2. Adjacency list.
3. BFS from 3 different users (visit order and number of vertexes reached) and a complete DFS (discovery order and cycles).
4. Queries: users without followers, most influential, most active, and reachability between users.
5. CRUD operations (add, delete and update), including rejected attempts, with the changes printed after each operation.

## Execution evidence

Below you will find the evidence as it is seen in the local terminal of the pc executing the code from Visual Studio Code:

```text
PS C:\Users\david\Desktop\UManizales\Semestre4\Programación3\Actividad2 revisada> python main.py

=== Graph construction ===
[createVertex] id=1, name=David, rol=student: vertex created
[createVertex] id=2, name=Sebastián, rol=student: vertex created
[createVertex] id=3, name=Carolina, rol=teacher: vertex created
[createVertex] id=4, name=Mariana, rol=graduate: vertex created
[createVertex] id=5, name=Luna, rol=student: vertex created
[createVertex] id=6, name=Alejandro, rol=teacher: vertex created
[createVertex] id=7, name=María José, rol=student: vertex created
[createVertex] id=8, name=Felipe, rol=graduate: vertex created
[createVertex] id=9, name=Aurora, rol=student: vertex created
[createVertex] id=10, name=Ricardo, rol=teacher: vertex created
[createVertex] id=11, name=Valentina, rol=graduate: vertex created
[createVertex] id=12, name=Santiago, rol=student: vertex created
[createEdge] 1 follows 2: relation created
[createEdge] 1 follows 3: relation created
[createEdge] 1 follows 4: relation created
[createEdge] 1 follows 5: relation created
[createEdge] 2 follows 3: relation created
[createEdge] 2 follows 6: relation created
[createEdge] 3 follows 4: relation created
[createEdge] 4 follows 1: relation created
[createEdge] 5 follows 6: relation created
[createEdge] 5 follows 7: relation created
[createEdge] 5 follows 8: relation created
[createEdge] 5 follows 9: relation created
[createEdge] 6 follows 7: relation created
[createEdge] 7 follows 8: relation created
[createEdge] 8 follows 5: relation created
[createEdge] 9 follows 11: relation created
[createEdge] 10 follows 1: relation created
[createEdge] 10 follows 5: relation created
[createEdge] 10 follows 9: relation created
[createEdge] 12 follows 11: relation created
[createEdge] 12 follows 9: relation created
Adjacency list of CampusNet:
  1 David (student) -> 2, 3, 4, 5
  2 Sebastián (student) -> 3, 6
  3 Carolina (teacher) -> 4
  4 Mariana (graduate) -> 1
  5 Luna (student) -> 6, 7, 8, 9
  6 Alejandro (teacher) -> 7
  7 María José (student) -> 8
  8 Felipe (graduate) -> 5
  9 Aurora (student) -> 11
  10 Ricardo (teacher) -> 1, 5, 9
  11 Valentina (graduate) -> -
  12 Santiago (student) -> 11, 9

=== Traversals ===
Breadth-first search (BFS) from user 1, visit order:
  1. 1 David (student)
  2. 2 Sebastián (student)
  3. 3 Carolina (teacher)
  4. 4 Mariana (graduate)
  5. 5 Luna (student)
  6. 6 Alejandro (teacher)
  7. 7 María José (student)
  8. 8 Felipe (graduate)
  9. 9 Aurora (student)
  10. 11 Valentina (graduate)
Vertexes reached: 10
Breadth-first search (BFS) from user 10, visit order:
  1. 10 Ricardo (teacher)
  2. 1 David (student)
  3. 5 Luna (student)
  4. 9 Aurora (student)
  5. 2 Sebastián (student)
  6. 3 Carolina (teacher)
  7. 4 Mariana (graduate)
  8. 6 Alejandro (teacher)
  9. 7 María José (student)
  10. 8 Felipe (graduate)
  11. 11 Valentina (graduate)
Vertexes reached: 11
Breadth-first search (BFS) from user 12, visit order:
  1. 12 Santiago (student)
  2. 11 Valentina (graduate)
  3. 9 Aurora (student)
Vertexes reached: 3
Complete depth-first search (DFS), discovery order:
  1. 1 David (student)
  2. 2 Sebastián (student)
  3. 3 Carolina (teacher)
  4. 4 Mariana (graduate)
  5. 6 Alejandro (teacher)
  6. 7 María José (student)
  7. 8 Felipe (graduate)
  8. 5 Luna (student)
  9. 9 Aurora (student)
  10. 11 Valentina (graduate)
  11. 10 Ricardo (teacher)
  12. 12 Santiago (student)
Vertexes discovered: 12
Cycles found: 4
  1 -> 2 -> 3 -> 4 -> 1
  6 -> 7 -> 8 -> 5 -> 6
  7 -> 8 -> 5 -> 7
  8 -> 5 -> 8

=== Social queries ===
Users without followers (in-degree 0):
  10 Ricardo (teacher)
  12 Santiago (student)
Most influential users (highest in-degree), degree 3:
  5 Luna (student)
  9 Aurora (student)
Most active users (highest out-degree), degree 4:
  1 David (student)
  5 Luna (student)
[canReach] user 1 can reach user 11: yes
[canReach] user 11 can reach user 1: no
[canReach] user 12 can reach user 10: no

=== CRUD operations ===
[createVertex] id=13, name=Mateo, rol=student: vertex created
Adjacency list of CampusNet:
  1 David (student) -> 2, 3, 4, 5
  2 Sebastián (student) -> 3, 6
  3 Carolina (teacher) -> 4
  4 Mariana (graduate) -> 1
  5 Luna (student) -> 6, 7, 8, 9
  6 Alejandro (teacher) -> 7
  7 María José (student) -> 8
  8 Felipe (graduate) -> 5
  9 Aurora (student) -> 11
  10 Ricardo (teacher) -> 1, 5, 9
  11 Valentina (graduate) -> -
  12 Santiago (student) -> 11, 9
  13 Mateo (student) -> -
[createVertex] id=13, name=Mateo, rol=student: rejected, repeated id (the vertex already exists)
[createEdge] 13 follows 5: relation created
Adjacency list of CampusNet:
  1 David (student) -> 2, 3, 4, 5
  2 Sebastián (student) -> 3, 6
  3 Carolina (teacher) -> 4
  4 Mariana (graduate) -> 1
  5 Luna (student) -> 6, 7, 8, 9
  6 Alejandro (teacher) -> 7
  7 María José (student) -> 8
  8 Felipe (graduate) -> 5
  9 Aurora (student) -> 11
  10 Ricardo (teacher) -> 1, 5, 9
  11 Valentina (graduate) -> -
  12 Santiago (student) -> 11, 9
  13 Mateo (student) -> 5
[createEdge] 13 follows 5: rejected, repeated relation (it already follows that user)
[createEdge] 13 follows 13: rejected, a user cannot follow itself
[deleteEdge] 13 stops following 5: relation deleted
Adjacency list of CampusNet:
  1 David (student) -> 2, 3, 4, 5
  2 Sebastián (student) -> 3, 6
  3 Carolina (teacher) -> 4
  4 Mariana (graduate) -> 1
  5 Luna (student) -> 6, 7, 8, 9
  6 Alejandro (teacher) -> 7
  7 María José (student) -> 8
  8 Felipe (graduate) -> 5
  9 Aurora (student) -> 11
  10 Ricardo (teacher) -> 1, 5, 9
  11 Valentina (graduate) -> -
  12 Santiago (student) -> 11, 9
  13 Mateo (student) -> -
[updateVertex] id=2, name=Juan Sebastián, rol=graduate: vertex updated
Adjacency list of CampusNet:
  1 David (student) -> 2, 3, 4, 5
  2 Juan Sebastián (graduate) -> 3, 6
  3 Carolina (teacher) -> 4
  4 Mariana (graduate) -> 1
  5 Luna (student) -> 6, 7, 8, 9
  6 Alejandro (teacher) -> 7
  7 María José (student) -> 8
  8 Felipe (graduate) -> 5
  9 Aurora (student) -> 11
  10 Ricardo (teacher) -> 1, 5, 9
  11 Valentina (graduate) -> -
  12 Santiago (student) -> 11, 9
  13 Mateo (student) -> -
[deleteVertex] id=5: vertex deleted (the relations that pointed to it were deleted too)
Adjacency list of CampusNet:
  1 David (student) -> 2, 3, 4
  2 Juan Sebastián (graduate) -> 3, 6
  3 Carolina (teacher) -> 4
  4 Mariana (graduate) -> 1
  6 Alejandro (teacher) -> 7
  7 María José (student) -> 8
  8 Felipe (graduate) -> -
  9 Aurora (student) -> 11
  10 Ricardo (teacher) -> 1, 9
  11 Valentina (graduate) -> -
  12 Santiago (student) -> 11, 9
  13 Mateo (student) -> -
[deleteVertex] id=99: rejected, id not found
PS C:\Users\david\Desktop\UManizales\Semestre4\Programación3\Actividad2 revisada>
```
