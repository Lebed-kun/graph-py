from graph import Graph

# Success 
def test_distance():
    graph = Graph([
        1, 2, 3, 4,
        5, 6, 7
    ])

    graph.addAdjacent(1, 2)\
        .addAdjacent(2, 3)\
        .addAdjacent(3, 7)\
        .addAdjacent(1, 5)\
        .addAdjacent(2, 6)\
        .addAdjacent(3, 6)\
        .addAdjacent(4, 5)\
        .addAdjacent(5, 6)

    distance = graph.distance(4, 3)
    print("Distance: " + str(distance))

# Success
def test_distance_matrix():
    graph = Graph([
        1, 2, 3, 4,
        5, 6, 7
    ])

    graph.addAdjacent(1, 2)\
        .addAdjacent(2, 3)\
        .addAdjacent(3, 7)\
        .addAdjacent(1, 5)\
        .addAdjacent(2, 6)\
        .addAdjacent(3, 6)\
        .addAdjacent(4, 5)\
        .addAdjacent(5, 6)

    distanceMatrix = graph.distanceMatrix()
    print(distanceMatrix)

# Success
def test_eccentricities():
    graph = Graph([
        1, 2, 3, 4,
        5, 6, 7
    ])

    graph.addAdjacent(1, 2)\
        .addAdjacent(2, 3)\
        .addAdjacent(3, 7)\
        .addAdjacent(1, 5)\
        .addAdjacent(2, 6)\
        .addAdjacent(3, 6)\
        .addAdjacent(4, 5)\
        .addAdjacent(5, 6)

    eccentricities = graph.eccentricities()
    print(eccentricities)

    distanceMatrix = graph.distanceMatrix()
    print(distanceMatrix)

# Success
def test_radius_diameter():
    graph = Graph([
        1, 2, 3, 4,
        5, 6, 7
    ])

    graph.addAdjacent(1, 2)\
        .addAdjacent(2, 3)\
        .addAdjacent(3, 7)\
        .addAdjacent(1, 5)\
        .addAdjacent(2, 6)\
        .addAdjacent(3, 6)\
        .addAdjacent(4, 5)\
        .addAdjacent(5, 6)

    eccentricities = graph.eccentricities()
    print(eccentricities)

    radius = graph.radius()
    print("Radius: {}".format(radius))

    diameter = graph.diameter()
    print("Diameter: {}".format(diameter))

# Success
def test_inverse():
    graph = Graph([1, 2, 3, 4])

    graph.addAdjacent(1, 2)\
        .addAdjacent(1, 3)\
        .addAdjacent(2, 4)

    inverse = graph.inverse()

    print("Original graph: ", graph.getVerticies())
    print("Inverse graph: ", inverse.getVerticies())

# Union of original and its inverse must be complete graph
# Success
def test_union():
    graph1 = Graph([1, 2, 3, 4])
    graph1.addAdjacent(1, 2)\
        .addAdjacent(1, 3)\
        .addAdjacent(2, 4)

    inverse1 = graph1.inverse()

    union1 = graph1.union(inverse1)

    graph2 = Graph(['a', 'b', 'c', 'd'])
    graph2.addAdjacent('a', 'b')\
        .addAdjacent('a', 'd')\
        .addAdjacent('c', 'd')

    union2 = graph1.union(graph2)

    print("Original graph: ", graph1.getVerticies())
    print("Inverse graph: ", inverse1.getVerticies())
    print("Union graph: ", union1.getVerticies())
    print("Second graph: ", graph2.getVerticies())
    print("Union of disjoint graphs: ", union2.getVerticies())

# 1. Intersection of original and its inverse must be graph without any edges;
# 2. Intersection of disjoint graphs must be empty graph;
# 3. Test intersection with common edges
# Success
def test_intersection():
    graph1 = Graph([1, 2, 3, 4])
    graph1.addAdjacent(1, 2)\
        .addAdjacent(1, 3)\
        .addAdjacent(2, 4)

    inverse1 = graph1.inverse()

    intersection1 = graph1.intersection(inverse1)

    print("Original graph: ", graph1.getVerticies())
    print("Inverse graph: ", inverse1.getVerticies())
    print("Intersection: ", intersection1.getVerticies())

    graph2 = Graph(['a', 'b', 'c', 'd'])
    graph2.addAdjacent('a', 'b')\
        .addAdjacent('a', 'd')\
        .addAdjacent('c', 'd')

    intersection2 = graph1.intersection(graph2)

    print("\nFirst graph: ", graph1.getVerticies())
    print("Second graph: ", graph2.getVerticies())
    print("Intersection: ", intersection2.getVerticies())

    graph3 = Graph([1, 2, 3, 4])
    graph3.addAdjacent(1, 2)\
        .addAdjacent(2, 3)\
        .addAdjacent(3, 4)\
        .addAdjacent(2, 4)

    intersection3 = graph1.intersection(graph3)

    print("\nFirst graph: ", graph1.getVerticies())
    print("Second graph: ", graph3.getVerticies())
    print("Intersection: ", intersection3.getVerticies())

# Success
def test_join():
    graph1 = Graph([1, 2])
    graph1.addAdjacent(1, 2)

    graph2 = Graph(['a', 'b', 'c'])
    graph2.addAdjacent('a', 'b')\
        .addAdjacent('b', 'c')

    join = graph1.join(graph2)

    print("First graph: ", graph1.getVerticies())
    print("Second graph: ", graph2.getVerticies())
    print("Join: ", join.getVerticies())

# Success
def test_product():
    graph1 = Graph(['x', 'y'])
    graph1.addAdjacent('x', 'y')

    graph2 = Graph(['a', 'b', 'c', 'd'])
    graph2.addAdjacent('a', 'b')\
        .addAdjacent('b', 'c')\
        .addAdjacent('c', 'd')

    product = graph1.product(graph2)

    print("First graph: ", graph1.getVerticies())
    print("Second graph: ", graph2.getVerticies())
    print("Product: ", product.getVerticies())

test_product()