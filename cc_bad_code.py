class Mapping:
    def __init__(self, e): 
        self.e = e # e is for edge (bad code - not using intention-revealing name)
        self.graphDict = {}
        for pointOfStartingDestination, pointOfEndingDestination in e:
            if pointOfStartingDestination in self.graphDict:
                self.graphDict[pointOfStartingDestination].append(pointOfEndingDestination)
            else:
                self.graphDict[pointOfStartingDestination] = [pointOfEndingDestination]


    def getPaths(self, path1, path2, path=[]): # path1 - start, path2- destination
        path = path + [path1]

        if path1 == path2: ## exit condition 1,
            return [path]

        if path1 not in self.graphDict: # exit condition 2
            return []

        paths = []
        for i in self.graphDict[path1]:
            if i not in path:
                transptd = self.getPaths(i, path2, path)
                for l in transptd:
                    paths.append(l)
        return paths

    def short(self, location, destination, path=[]):
        path = path + [location]

        if location == destination: ## exit condition 1
            return path

        if location not in self.graphDict: # exit condition 2
            return []

        shortestPath = None
        for zoom in self.graphDict[location]:
            if zoom not in path:
                shortestTransit = self.short(zoom, destination, path)
                if shortestTransit:
                    if shortestPath is None or len(shortestTransit) < len(shortestPath):
                        shortestPath = shortestTransit
        return shortestPath

    def retrieveShortestPath(self, location, destination, path=[]):
        path = path + [location]

        if location == destination: ## exit condition 1
            return path

        if location not in self.graphDict: # exit condition 2
            return []

        shortestPath = None
        for zoom in self.graphDict[location]:
            if zoom not in path:
                shortestTransit = self.short(zoom, destination, path)
                if shortestTransit:
                    if shortestPath is None or len(shortestTransit) < len(shortestPath):
                        shortestPath = shortestTransit
        return shortestPath

if __name__ == '__main__':

    mapPlaces = [
        ("BSB", "Paris"),
        ("BSB", "Dubai"),
        ("Paris", "Dubai"),
        ("Paris", "New York"),
        ("Dubai", "New York"),
        ("New York", "Toronto"),
    ]
theMap = Mapping(mapPlaces)

start = "BSB"
destination = "New York"

print(f"All paths between: {start} and {destination}", theMap.getPaths(start, destination))

print(f"Shortest path between: {start} and {destination}", theMap.short(start, destination))

"""
bad code 1 
- not using intention-revealing name:
in line 3, where e reveals nothing.

- causing disinformation:
from line 5 to 9,
if compare side to side pointOfStartingDestination, with
pointOfEndingDestination, they have quite similar shapes.

- class name:
in line 1, using verb "Mapping" as the class name.
a cleaner code would use Graph.    

- not making meaningful distinctions:
in line 12, where path1 and path2 is used, 
not making the names different and meaningful.

- not using pronounceable names:
in line 24, using transptd (for trasnit path to destination), 
people end up saying "trans-p-t-d".

- notusing searchable names:
in line 22, i (for intermediate), hence 'i' is a poor choice 
for searching variable.

- doing mental mapping:
in line 25, the use of l in some environment may seem as the number 1.

- method name:
in line 29, using a verb "short". 
The cleaner code would use getShortestPath.

- by being cute:
in line 39, using "zoom" which doesn't have any meaning. 
(say what you mean. mean what you say)

- didn't pick one word per concept:
in line 12 and 47, using 2 concepts of 'retirve' and 'get' 
which are equivalent methods.

- using gratuitous Context
in line 67, "mapPlaces" to add context to things that are already clear.

- not adding meaningful context
in line 75, using theMap as the name of variable. cleaner code would use "routeGraph".

- using pun:
in line 75, having 3 variable associating with maps and naming them with map might confuse the reader.
"""
######################################################
import random 
key1 = [] 
while len(key1) <10: 
	while True: 
		candidate = random.randint(10,19) 
		if candidate in key1: 
			continue 
		key1.append(candidate) 

key2 = [] 
while len(key2) <10: 
	while True: 
		candidate = random.randint(0, 9) 
		if candidate in key2: 
			continue 
		key2.append(candidate) 
"""
bad code 2
- not keeping it Small
to build 2 lists of keys. 
key 1 the values 0 to 9 in random order, 
key2 the values 10 to 19 in random order.
"""

#######################################################
class Queue:
    DEFAULT = 10 #N
    
    def __init__(self):
        self.data = [None] * Queue.DEFAULT #N
        self.size = 0 #elements inside the queue

    def addData(self,value):
        #add a new element (value) to the rear of the queue
        if self.size == Queue.DEFAULT:
            raise Exception('Queue is Full') #it print and returns 

        rear = (self.front + self.size) % Queue.DEFAULT
        self.data[rear] = value
        self.size += 1

        if self.size == 0:
            print("Queue is empty")
        else:
            return self.size

qq = Queue()
word = 'stressed'
for i in range (len(word)):
    qq.addData(word[i])
print(qq.data)

"""
bad code 3
- do one thing 
in function addData it does a lot of things from adding value, 
checking if queue is empty and finding the size.

- have descriptive name
in line 161, default what? make it clear (DEFAULT_CAPACITY)
"""
