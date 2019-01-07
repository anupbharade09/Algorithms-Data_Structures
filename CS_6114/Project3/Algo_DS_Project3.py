import collections
from collections import defaultdict

#a queue class
class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        return self.items.pop(0)

    def isEmpty(self):
        return len(self.items) == 0

class Graph:

    def __init__(self,vertices,edgesCount):

        self.graph = defaultdict(list)
        self.graph1 = defaultdict(list)
        self.V = vertices
        self.distances = {}
        self.nodes = set()
        self.edges = defaultdict(list)
        self.items = collections.OrderedDict()
        self.verticesCount = vertices
        self.edgesCount = edgesCount
        self.length = len(self.items)

    # function to add an edge to graph with weights

    def addEdge(self, u, v,distance):
        self.graph1[u].append((v, distance))
        self.graph[u].append(v)
        self.edges[u].append(v)
        self.nodes.add(v)
        #to store distances of edges
        self.distances[(u, v)] = distance
        if u in self.items.keys():
            self.items[u].append(v)
        else:
            self.items[u] = [v]
        # update length
        self.length = len(self.items)

        # Function to print a BFS of graph

    def BFS(self, s):
        # Mark all the vertices as not visited
        visited = []
        # Create a queue for BFS
        queue = []
        # Mark the source node as visited and enqueue it
        queue.append(s)
        #print(self.graph)
        visited.append(s)
        while queue:

            # Dequeue a vertex from queue and print it
            s = queue.pop(0)
            print(s, end=" ")

            # Get all adjacent vertices of the dequeued vertex s. If a adjacent has not been visited, then mark it visited and enqueue it
            for i in self.graph[s]:
                if i not in visited:
                    queue.append(i)
                    visited.append(i)
        # A function used by DFS

    def DFSrecur(self, v, visited):
        # Mark the current node as visited and print it
        visited.append(v)
        print(v,end=' ')
        # Recur for all the vertices adjacent to this vertex
        for i in self.graph[v]:
            if i not in visited:
                self.DFSrecur(i, visited)

    # The function to do DFS traversal. It uses recursive DFSrecur()

    def DFS(self, v):
        # Mark all the vertices as not visited
        visited = []

        # Call the recursive helper function to print DFS traversal
        self.DFSrecur(v, visited)

    def recur(self, v, visited, recStack):
        # Mark current node as visited and adds to recursion stack
        visited.append(v)
        recStack.append(v)

        # Recur for all neighbours if any neighbour is visited and in recStack then graph is cyclic

        for neighbour in self.graph[v]:
            if neighbour not in visited:
                if self.recur(neighbour, visited, recStack) == True:
                    return True
            elif neighbour in recStack:
                return True

        # The node needs to be poped from
        # recursion stack before function ends
        recStack.remove(v)
        return False

    # Returns true if graph is cyclic else false
    def isCyclic(self):
        visited = []
        #recStack = [False] * self.V
        recStack = []
        for node in range(self.V):
            #if visited[node] == False:
            if node not in visited:
                if self.recur(node, visited, recStack) == True:
                    return True
        return False

    def recur1(self, v, visited, parent):
        # Mark current node as visited
        visited.append(v)
        # Recur for all the vertices adjacent for this vertex
        for i in self.graph[v]:
            # If an adjacent is not visited, then recur for that adjacent
            if i not in visited:
                if self.recur1(i, visited, v) == True:
                    return True
            # If an adjacent is visited and not parent of current vertex, then there is a cycle.
            elif i != parent:
                return True
        return False
        # Returns true if the graph is a tree, else false.

    def isTree(self, root):
        # Mark all the vertices as not visited and not part of recursion stack
        visited = []
        # The call to recur1 function
        if self.recur1(root, visited, -1) == True:
            return False
        # If we find a vertex which is not reachable from 0 (not marked by recur(), then we return false
        for i in self.graph[root]:
            if i not in visited:
                return False
        return True


    def isBipartite(self):
        if self.edgesCount <= 1:
            return True
        graph_depth = collections.OrderedDict()
        visited = collections.OrderedDict()
        queue = Queue()

        # Initialize source node data
        parentNode = list(self.items.keys())[0]
        graph_depth[parentNode] = 0
        queue.enqueue(parentNode)
        while (queue.isEmpty() == False):
            parentNode = queue.dequeue()
            # Check if key exists, will throw error attempting to search for nonexistent key
            if parentNode in self.items.keys():
                # BFS: search all neighbors/edges for currentNode
                for currentNode in self.items[parentNode]:
                    if currentNode not in visited.keys():
                        visited[currentNode] = True
                        queue.enqueue(currentNode)
                        graph_depth[currentNode] = graph_depth[parentNode] + 1

                    # if a child of current node has already been visited & are both within same graph depth an odd cycle length exists
                    elif graph_depth[currentNode] == graph_depth[parentNode]:
                        return False

        # graph is bipartite if uninterrupted
        return True

# Print shortest path from each node
def dijkstra(graph, initial):
    visited = {initial: 0}
    path = defaultdict(list)
    nodes = set(graph.nodes)
    nodes.add(initial)

    while nodes:
        min_node = None
        for node in nodes:
            if node in visited:
                if min_node is None:
                    min_node = node
                elif visited[node] < visited[min_node]:
                    min_node = node

        if min_node is None:
            break

        nodes.remove(min_node)
        current_weight = visited[min_node]

        for edge in graph.edges[min_node]:
            weight = current_weight + graph.distances[(min_node, edge)]
            if edge not in visited or weight < visited[edge]:
                visited[edge] = weight
                if edge in path:
                    path[edge].pop(0)
                    path[edge].append(min_node)
                else:
                    path[edge].append(min_node)

    # print shortest distance
    print('Shortest distance from source to each node is: ')
    for i in visited:
        print(s,end=' --> ')
        print(i,end=': ')
        print(visited[i])

    # print predecessors value
    print('Predecessor of each node: ')
    for i in path:
        print('Predecessor of node',i,end=': ')
        print(path[i])

    return visited,path

# Main code

if __name__ == "__main__":
    print('Welcome to this program')
    print('You may use following operations to create Directed Graphs: ')
    print(' 1. Create Graph \n 2. DFS Traversal \n 3. BFS Traversal \n 4. Shortest Path between verties using Dijkstra algorithm \n '
          '5. Detect cycle in graph \n 6. Check graph is Bipartite or not \n 7. Check graph is tree or not \n 8. Exit')
    while True:
        choice = input(('Enter number for above operations: '))
        if choice == '1':
            v= int(input(('Number of vertices in graph: >')))
            maxLengthList = int(input('Total number of edges: '))
            if maxLengthList > v*(v-1):
                print('Number of edges can not exceed n*(n-1) , where n is number of vertices')
                maxLengthList = int(input('Please enter valid number of edges: '))

            g = Graph(v,maxLengthList)
            inlist = []
            vertice_list = []

            print('Press enter after every input')
            while len(inlist) < maxLengthList:
                try:
                    item = input("Enter vertices with their weights(0,1,3). Note: Vertices should be numeric: ")
                    item_list = item.split(',')
                    if not item:
                        raise ValueError('Empty value !! Please enter correct values')
                    elif not item_list[0].isdigit() or not item_list[1].isdigit():
                        raise ValueError('Please enter numeric values')
                    elif item_list[2] == '':
                        raise ValueError('Distance can not be null')
                    else:
                        inlist.append(item)
                except ValueError as e:
                        print(e)
                        continue
            for i in inlist:
                a = i.split(',')
                g.addEdge(int(a[0]), int(a[1]),int(a[2]))
                if int(a[0]) not in vertice_list:
                    vertice_list.append(int(a[0]))
                if int(a[1]) not in vertice_list:
                    vertice_list.append(int(a[1]))
                #g.addEdge(int(a[0]),int(a[1]))
        elif choice == '2':
            try:
                i = int(input('Type element from which DFS needs to be traversed: '))
                if i not in vertice_list:
                    raise ValueError('Such node does not exist')
                else:
                    print('Following is Depth First Traversal. Starting from vertex', i, ':\n')
                    g.DFS(i)
                    print('\n')
            except ValueError as e:
                print(e)
                continue
        elif choice == '3':
            try:
                i = int(input('Type element from which BFS needs to be traversed: '))
                if i not in vertice_list:
                    raise ValueError('Such node does not exist')
                else:
                    print('Following is Breadth First Traversal. Starting from vertex', i, ':\n')
                    g.BFS(i)
                    print('\n')
            except ValueError as e:
                print(e)
                continue
        elif choice == '4':
            try:
                s = int(input("Please enter the source element:> "))
                if s not in vertice_list:
                    raise ValueError('Such node does not exist')
                else:
                    dijkstra(g, s)
                    print('\n')
            except ValueError as e:
                print(e)
                continue
        elif choice == '5':
            if g.isCyclic() == 1:
                print("Graph has a cycle")
            else:
                print("Graph has no cycle")
        elif choice == '6':
            if (g.isBipartite()):
                print('Yes it is Bipartite graph')
            else:
                print('Not it is not a Bipartite graph')
        elif choice == '7':
            root = int(input('what is the root vertex of graph: '))
            if g.isTree(root) == True:
                print('Given graph is tree')
            else:
                print('Given graph is not a tree')
        elif choice == '8':
            break
        else:
            print('Please enter valid input: ')
