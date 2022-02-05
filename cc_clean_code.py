# clean code 1 ################################
class Graph:
    def __init__(self, edges):
        self.edges = edges
        self.graphDict = {}
        for start, destination in edges:
            if start in self.graphDict:
                self.graphDict[start].append(destination)
            else:
                self.graphDict[start] = [destination]
                #print("Graph Dict:", self.graphDict)

    def getPaths(self, start, destination, path=[]):
        path = path + [start]

        if start == destination: ## exit condition 1,
            return [path]

        if start not in self.graphDict: # exit condition 2
            return []

        paths = []
        for intermediate in self.graphDict[start]:
            if intermediate not in path:
                transitPaths = self.getPaths(intermediate, destination, path)
                for p in transitPaths:
                    paths.append(p)
        return paths

    def getShortestPath(self, start, destination, path=[]):
        path = path + [start]

        if start == destination: ## exit condition 1
            return path

        if start not in self.graphDict: # exit condition 2
            return []

        shortestPath = None
        for intermediate in self.graphDict[start]:
            if intermediate not in path:
                shortestTransit = self.getShortestPath(intermediate, destination, path)
                if shortestTransit:
                    if shortestPath is None or len(shortestTransit) < len(shortestPath):
                        shortestPath = shortestTransit
        return shortestPath

if __name__ == '__main__':

    routes = [
        ("BSB", "Paris"),
        ("BSB", "Dubai"),
        ("Paris", "Dubai"),
        ("Paris", "New York"),
        ("Dubai", "New York"),
        ("New York", "Toronto"),
    ]
routesGraph = Graph(routes)

start = "BSB"
destination = "New York"

print(f"All paths between: {start} and {destination}", routesGraph.getPaths(start, destination))

print(f"Shortest path between: {start} and {destination}", routesGraph.getShortestPath(start, destination))


# clean code 2 ################################
import random 
keys = [random.sample( range(index*10, (index+1)*10), 10) for index in range(0,7)] 


# clean code 3 ################################
class Queue:
    DEFAULT_CAPACITY = 10 #N
    
    def __init__(self):
        self.data = [None] * Queue.DEFAULT_CAPACITY #N
        self.size = 0 #elements inside the queue
        self.front = 0
    
    def Size(self):
        #returns the number of elements in the queue
        return self.size

    def is_empty(self):
        #returns True is the queue is empty
        return self.size == 0

    def enqueue(self,value):
        #add a new element (value) to the rear of the queue
        if self.size == Queue.DEFAULT_CAPACITY:
            raise Exception('Queue is Full') #it print and returns 

        rear = (self.front + self.size)%Queue.DEFAULT_CAPACITY
        self.data[rear] = value
        self.size += 1

qq = Queue()
word = 'stressed'
for i in range (len(word)):
    qq.enqueue(word[i])
print(qq.data)