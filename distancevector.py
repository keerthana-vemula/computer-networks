#AIM:WRITE A PROGRAM TO IMPLEMENT DISTANCEVECTOR

PROGRAM:
import numpy as np


class DistanceTable:
    def __init__(self, size):
        self.destination = list(range(size))
        self.distance = list(range(size))

class DistanceVector:
    def __init__(self):
        self.numberOfNodes, self.numberOfPaths = map(
            int, input("Enter number of nodes, paths : ").split()
        )
        self.graph = np.zeros((self.numberOfNodes, self.numberOfNodes), dtype=int)
        self.nodes = [DistanceTable(self.numberOfNodes) for i in range(self.numberOfNodes)]
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

        for i in range(self.numberOfNodes):
            for j in range(self.numberOfNodes):
                if self.graph[i][j] == 0 and i!=j:
                    self.nodes[i].distance[j] = 100000
                else:
                    self.nodes[i].distance[j] = self.graph[i][j]
                self.nodes[i].destination[j] = j

    def DV(self):
        while True:
            flag = False
            for i in range(self.numberOfNodes):
                for j in range(self.numberOfNodes):
                  for k in range(self.numberOfNodes):
                      if self.nodes[i].distance[j] > self.graph[i][k] + self.nodes[k].distance[j]:
                          flag = True
                          self.nodes[i].distance[j] = self.nodes[i].distance[k] + self.nodes[k].distance[j]
                          self.nodes[i].destination[j] = k
            if flag: break

        for i in range(self.numberOfNodes):
            print('For router',i+1)
            for j in range(self.numberOfNodes):
                print("node %d via %d Distance %d "%(j+1,self.nodes[i].destination[j]+1,self.nodes[i].distance[j]))


if __name__ == '__main__':
    d = DistanceVector()
    d.DV()



"""
OUTPUT:
Enter number of nodes, paths : 4 5
Enter source, destination, weight of path - 1 : 0 1 4
Enter source, destination, weight of path - 2 : 1 2 6
Enter source, destination, weight of path - 3 : 2 3 5
Enter source, destination, weight of path - 4 : 3 0 3
Enter source, destination, weight of path - 5 : 3 1 4
For router 1
node 1 via 1 Distance 0 
node 2 via 2 Distance 4 
node 3 via 4 Distance 8 
node 4 via 4 Distance 3 
For router 2
node 1 via 1 Distance 4 
node 2 via 2 Distance 0 
node 3 via 3 Distance 6 
node 4 via 4 Distance 4 
For router 3
node 1 via 4 Distance 8 
node 2 via 4 Distance 9 
node 3 via 3 Distance 0 
node 4 via 4 Distance 13 
For router 4
node 1 via 1 Distance 3 
node 2 via 2 Distance 4 
node 3 via 3 Distance 5 
node 4 via 4 Distance 0
"""
