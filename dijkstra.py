#AIM:WRITE A PROGRAM TO IMPLEMENT DIJKSTRA'S ROUTING ALGORITHM

import numpy as np

class Dijkstra:
    def __init__(self):
        self.numberOfNodes, self.numberOfPaths = map(
            int, (input("Enter number of nodes, paths: ").split())
        )
        self.cost = [1000000 for i in range(self.numberOfNodes)]
        self.parent = [i for i in range(self.numberOfNodes)]
        self.visited = [False for i in range(self.numberOfNodes)]
        self.graph = np.zeros((self.numberOfNodes, self.numberOfNodes), dtype=int)
        for i in range(self.numberOfPaths):
            source, destination, weight = list(
                map(
                    int,
                    input(
                        f"Enter source, destination, weight of path - {i+1} : "
                    ).split(),
                )
            )
            self.graph[source][destination] = weight
            self.graph[destination][source] = weight
        self.source = int(input("Enter source vertex: "))
        self.destination = int(input("Enter destination vertex: "))

    def getPath(self, path, parent, vertex):
        if parent[vertex] == vertex:
            return str(vertex) + "->" + path
        else:
            return self.getPath(str(vertex) + "->" + path, parent, parent[vertex])

    def minKey(self):
        minIndex, minDistance = -1, 1000000
        for i in range(self.numberOfNodes):
            if self.cost[i] < minDistance and not self.visited[i]:
                minIndex = i
                minDistance = self.cost[i]
        return minIndex

    def findShortPath(self):
        self.cost[self.source] = 0
        count = 0
        while count != self.numberOfNodes:
            min = self.minKey()
            self.visited[min] = True
            for i in range(self.numberOfNodes):
                temp = self.cost[min] + self.graph[min][i]
                if (
                    not self.visited[i]
                    and temp < self.cost[i]
                    and self.graph[min][i] != 0
                ):
                    self.parent[i] = min
                    self.cost[i] = temp
            count += 1


if __name__ == "__main__":
    d = Dijkstra()
    d.findShortPath()
    print(f"Cost from {d.source} to {d.destination} is {d.cost[d.destination]}")
    print(f"Path is {d.getPath('',vertex = d.destination, parent = d.parent).rstrip('->')}")







"""
OUTPUT:
Enter number of nodes, paths: 4 5
Enter source, destination, weight of path - 1 : 0 1 2
Enter source, destination, weight of path - 2 : 1 2 4
Enter source, destination, weight of path - 3 : 2 3 3
Enter source, destination, weight of path - 4 : 3 0 3
Enter source, destination, weight of path - 5 : 1 3 4
Enter source vertex: 0
Enter destination vertex: 3
Cost from 0 to 3 is 3
Path is 0->3
"""
