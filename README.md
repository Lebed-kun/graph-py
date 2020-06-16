# Graph

Unoriented graph based on list of adjacent verticies

## Constructor(verticies)

- verticies: list of graph verticies;

## Methods

### getVerticies()

- Get adjacenty list of a graph

### getAdjacents(vertex)

- vertex: number or string or another primitive type
- Get list of adjacent verticies for given vertex

### setAdjacents(vertex, adjacents)

- vertex: number or string or another primitive type
- adjacents: list of verticies
- Set list of adjacent verticies for given vertex

### addAdjacent(source, destination)

- source: start vertex
- destination: end vertex
- Add an edge (source, destination) to a graph

### distance(source, destination)

- source: start vertex
- destination: end vertex
- Get the least number of edges that connects source and destination

### distanceMatrix()

- Get distances in all pairs of graph's verticies

### eccentricities()

- Get eccentricities of graph's verticies

### radius()

- Get minimum eccentricity of a graph

### diameter()

- Get maximum eccentricity of a graph

### inverse()

- Get inverse of a graph

### union(graph)

- graph: given graph
- Get union of current and given graphs

### intersection(graph)

- graph: given graph
- Get intersection of current and given graphs

### join(graph)

- graph: given graph
- Get join of current and given graphs

### product(graph)

- graph: given graph
- Get cartesian product of current and given graphs

### composition(graph)

- graph: given graph
- Get composition (lexicographical product) of current and given graphs

