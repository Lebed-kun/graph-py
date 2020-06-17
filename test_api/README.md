# Request data format

For unary operations (like radius, diameter, inverse etc.):

```
{
    "action": <name_of_method>,
    "data": {
        "graph": <adjacenty_list_of_verticies>
    }
}
```

For binary operations (like union, join, product etc.):

```
{
    "action": <name_of_method>,
    "data": {
        "graph": <adjacenty_list_of_verticies>,
        "graph2": <adjacenty_list_of_verticies>
    }
}
```

## List of available acions

For their purpose see root README. They are same as core lib's methods.

- distanceMatrix;
- eccentricities
- radius;
- diameter;
- inverse;
- union;
- intersection;
- join;
- product;
- composition;

# Response data format

```
{
    "type": <data_type>,
    "data": <data_returned_from_action>
}
```

## Types of data

- graph: a map from nodes/verticies (string) to list of neighbor nodes/verticies;
- matrix: a map from nodes/verticies (string) to a map from neighbor nodes to numbers;
- list: a map from nodes/verticies to numbers (scalars);
- number: an integer number, scalar property of graph;