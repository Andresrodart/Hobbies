import heapq

class Graph:
    def __init__(self, nNodes):
        self.nNodes = nNodes
        self.edges = [ dict() for _ in range(nNodes)]
    def addEdge(self, nodeA, nodeB, w=1):
        self.edges[nodeA][nodeB] = w
    def dijiktra(self, start):
        nodesToVisit = [(0, start)]
        nodesVisted = set()
        distances = [int('inf')] * self.nNodes

        while nodesToVisit:
            w, node =  heapq.heappop(nodesToVisit)
            if node not in nodesVisted:
                nodesVisted.add(node)
                for child in self.edges[node].key():
                    newDistance = w + self.edges[node][child]
                    distances[node] = min(newDistance, distances[node])
                    heapq.heappush(nodesToVisit, (distances[node], child))
        return distances

def getMinDistancesBetweennodes(origin, destination, nVertices, edges):
    graph = Graph(nVertices)
    for edge in edges:
        graph.addEdge(edge[0], edge[1], edge[2])
    return graph.dijiktra(origin)[destination]


            
