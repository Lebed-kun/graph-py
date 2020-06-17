import json
from graph import Graph 

class Parser:
    _data = None 

    def __init__(self, rawData):
        self._data = json.loads(rawData)

    def _makeGraph(self, rawData):
        graph = Graph(rawData)

        for vertex in rawData:
            for adjacent in rawData[vertex]:
                graph.addAdjacent(vertex, adjacent)

        return graph

    def _performAction(self):
        if not "action" in self._data:
            raise ValueError("Data must have action!")
        if not "data" in self._data:
            raise ValueError("Data must have parameters!")
        if not "graph" in self._data["data"]:
            raise ValueError("Data parameters must have a source graph!")

        graph = self._makeGraph(self._data["data"]["graph"])
        graph2 = None

        if "graph2" in self._data["data"]:
            graph2 = self._makeGraph(self._data["data"]["graph2"])

        result = getattr(graph, self._data["action"])(
            graph2
        )

        return result

    def _listifyAdjacents(self, graph):
        verticies = graph.getVerticies()

        for vertex in verticies:
            verticies[vertex] = list(verticies[vertex])

        return verticies

    def parse(self):
        result = {}
        newData = self._performAction()

        if isinstance(newData, Graph):
            result["type"] = "graph"
            result["data"] = self._listifyAdjacents(newData)
        elif isinstance(newData, dict) and\
            self._data["action"] == "distanceMatrix":
            result["type"] = "matrix"
            result["data"] = newData
        elif isinstance(newData, dict) and\
            self._data["action"] == "eccentricities":
            result["type"] = "list"
            result["data"] = newData
        else:
            result["type"] = "number"
            result["data"] = newData

        return json.dumps(result)

