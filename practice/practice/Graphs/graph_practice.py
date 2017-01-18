"""
WAP to find if the node is reachable from graph.
Implement an algorithm for Breadth first search and depth first search.
"""
from collections import defaultdict


class Graph(object):
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = defaultdict(list)

    def add_edge(self, start, end):
        self.graph[start].append(end)

    def breadth_first_search(self, start):
        visited = [False]* self.vertices
        queue = [start]
        visited[start] = True
        while queue:
            s = queue.pop()
            print s,
            for i in self.graph[s]:
                if not visited[i]:
                    queue.append(i)
                    visited[i] = True

    def depth_first_search(self, start):
        visited = [False]*self.vertices
        self.dfs_util(start, visited)

    def dfs_util(self, start, visited):
        visited[start] = True
        print start,
        for i in self.graph[start]:
            if not visited[i]:
                self.dfs_util(i, visited)

g = Graph(4)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(2, 3)
g.add_edge(3, 3)
print "BFS:", g.breadth_first_search(2)
print "DFS:", g.depth_first_search(2)