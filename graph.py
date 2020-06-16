class Graph:
    _adjVerticies = None # { [vertex: number] : number[] }
    _memoized = {
        'distanceMatrix' : None, # { [vertex: number] : { [vertex: number] : number  } }
        'eccentricities' : None # { [vertex: number] : number }
    }

    def __init__(self, verticies):
        adjVerticies = {}
        
        for vertex in verticies:
            adjVerticies[vertex] = set()

        self._adjVerticies = adjVerticies
    
    def _makeDirty(self):
        for key in self._memoized:
            self._memoized[key] = None

    def _safeMin(self, number1, number2):
        if number1 is None:
            return number2
        elif number2 is None:
            return number1
        else:
            return number1 if number1 < number2 else number2

    def _safeMax(self, number1, number2):
        if number1 is None:
            return number2
        elif number2 is None:
            return number1
        else:
            return number1 if number1 > number2 else number2

    def getVerticies(self):
        return self._adjVerticies

    def getAdjacents(self, vertex):
        return self._adjVerticies[vertex]

    def setAdjacents(self, vertex, adjacents):
        if vertex in self._adjVerticies:\
           self._adjVerticies[vertex] = adjacents

        self._makeDirty()
        return self

    def addAdjacent(self, source, destination):
        if not source in self._adjVerticies:
            self._adjVerticies[source] = set()
        if not destination in self._adjVerticies:
            self._adjVerticies[destination] = set()

        if not destination in self._adjVerticies[source]:
            self._adjVerticies[source].add(destination)
        if not source in self._adjVerticies[destination]:
            self._adjVerticies[destination].add(source)

        self._makeDirty()
        return self

    def distance(self, source, destination):
        result = None

        currVertex = source
        currLength = 0
        visited = set()
        stack = []

        while True:
            if len(stack) > 0:
                currVertex, currLength = stack.pop()

            if currVertex == destination:
                result = self._safeMin(currLength, result)

            # Mark as visited
            visited.add(currVertex)

            # Push unvisited neighbors to the stack
            neighbors = self._adjVerticies[currVertex]
            for vertex in neighbors:
                if not (vertex in visited):
                    stack.append((vertex, currLength + 1))

            # If stack stays empty after above operation
            # then algorithm terminates
            if len(stack) == 0:
                return result

    def distanceMatrix(self):
        if self._memoized['distanceMatrix'] is not None:
            return self._memoized['distanceMatrix']

        self._memoized['distanceMatrix'] = {}

        for source in self._adjVerticies:
            self._memoized['distanceMatrix'][source] = {}
            
            for destination in self._adjVerticies:
                distance = self.distance(source, destination)
                self._memoized['distanceMatrix'][source][destination] = distance

        return self._memoized['distanceMatrix']

    def eccentricities(self):
        if self._memoized['eccentricities'] is not None:
            return self._memoized['eccentricities']

        self._memoized['eccentricities'] = {}
        distanceMatrix = self.distanceMatrix()

        for source in distanceMatrix:
            eccentricity = None
            for destination in distanceMatrix[source]:
                eccentricity = self._safeMax(
                    distanceMatrix[source][destination],
                    eccentricity
                )
            self._memoized['eccentricities'][source] = eccentricity

        return self._memoized['eccentricities']

    def radius(self):
        result = None
        
        eccentricities = self.eccentricities()

        for vertex in eccentricities:
            result = self._safeMin(
                eccentricities[vertex],
                result
            )

        return result

    def diameter(self):
        result = None
        
        eccentricities = self.eccentricities()

        for vertex in eccentricities:
            result = self._safeMax(
                eccentricities[vertex],
                result
            )

        return result

    # @return {Graph}
    def inverse(self):
        inverse = (type(self))(
            self._adjVerticies
        )
        
        for source in self._adjVerticies:
            for destination in self._adjVerticies:
                if source != destination and not (
                    destination in self._adjVerticies[source]
                ):
                    inverse.addAdjacent(source, destination)

        return inverse

    # @return {Graph}
    def union(self, graph):
        verticies = graph.getVerticies()
        
        union = (type(self))(
            set(self._adjVerticies).union(
                set(verticies)
            )
        )

        # Iterate over self verticies
        for vertex in self._adjVerticies:
            if vertex in verticies:
                union.setAdjacents(
                    vertex,
                    self.getAdjacents(vertex).union(
                        graph.getAdjacents(vertex)
                    )
                )
            else:
                union.setAdjacents(
                    vertex,
                    self.getAdjacents(vertex) 
                )

        # Iterate over graph's verticies
        for vertex in verticies:
            if vertex in self._adjVerticies:
                union.setAdjacents(
                    vertex,
                    graph.getAdjacents(vertex).union(
                        self.getAdjacents(vertex)
                    )
                )
            else:
                union.setAdjacents(
                    vertex,
                    graph.getAdjacents(vertex)
                )

        return union

    def intersection(self, graph):
        verticies = grapg.getVerticies()

        intersection = (type(self))(
            set(self._adjVerticies).intersection(
                set(verticies)
            )
        )
        
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

