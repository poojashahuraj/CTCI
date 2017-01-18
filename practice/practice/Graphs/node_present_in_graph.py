from collections import defaultdict


class Graph(object):
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = defaultdict(list)

    def add_edge(self, start, end):
        self.graph[start].append(end)

    def breadth_first_search(self, start, dest):
        visited = [False] * self.vertices
        queue = [start]
        visited[start] = True
        while queue:
            s = queue.pop()
            if s == dest:
                return True
            for i in self.graph[s]:
                if not visited[i]:
                    queue.append(i)
                    visited[i] = True
        return False

    def depth_first_search(self, start):
        visited = [False] * len(self.graph)
        self.util_dfs(start, visited)

    def util_dfs(self, start, visited):
        visited[start] = True
        print start,
        for i in self.graph[start]:
            if not visited[i]:
                self.util_dfs(i, visited)

g = Graph(4)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(2, 3)
g.add_edge(3, 3)

u = 1
v = 3

if g.breadth_first_search(u, v):
    print("There is a path from %d to %d" % (u, v))
else:
    print("There is no path from %d to %d" % (u, v))

u = 3
v = 1
if g.breadth_first_search(u, v):
    print("There is a path from %d to %d" % (u, v))
else:
    print("There is no path from %d to %d" % (u, v))

g.depth_first_search(2)