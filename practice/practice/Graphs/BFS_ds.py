from collections import defaultdict


class BFS(object):
    def __init__(self, nodes):
        self.nodes = nodes
        self.graph = defaultdict(list)
        pass

    def add_edge(self, source, dest):
        self.graph[source].append(dest)

    def breadth_first_search_correct(self, start):
        visited = [False]* self.nodes
        queue = [start]
        visited[start] = True
        while queue:
            s = queue.pop()
            print s,
            for i in self.graph[s]:
                if not visited[i]:
                    queue.append(i)
                    visited[i] = True

    def breadth_first_search(self, source):
        visited = [False]*self.nodes
        queue = [source]
        while queue:
            popped = queue.pop(0)
            print popped,
            visited[popped] = True
            for i in self.graph[popped]:
                if not visited[i]:
                    queue.append(i)
                    visited[i] = True

    def depth_first_traversal(self, source):
        visited = [False]*self.nodes
        self.dfs_util(source, visited)

    def dfs_util(self, source, visited):
        visited[source] = True
        print source,
        for i in self.graph[source]:
            if not visited[i]:
                visited[i] = True
                self.dfs_util(i, visited)

g = BFS(4)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(2, 3)
g.add_edge(3, 3)
print "BFS correct:", g.breadth_first_search_correct(2)
print "BFS:        ", g.breadth_first_search(2)
print "DFS:        ", g.depth_first_traversal(2)

"""
BFS: 2 3 0 1
DFS: 2 0 1 3
"""