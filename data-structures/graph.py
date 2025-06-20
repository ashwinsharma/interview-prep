from tabulate import tabulate
from collections import deque

class Graph:
    def __init__(self):
        self.adj_list = {}
    
    def __str__(self):
        n = len(self.adj_list)
        vertex_index_map = dict([(v, i) for i, v in enumerate(self.adj_list.keys())])
        adj_mat = [[0] * n for _ in range(n)]
        
        for v1, i in vertex_index_map.items():
            for v2 in self.adj_list[v1]:
                j = vertex_index_map[v2]
                adj_mat[i][j] = 1
        
        row_headers = col_headers = list(vertex_index_map.keys())
        adj_mat_with_row_headers = [[i] + row for i, row in zip(row_headers, adj_mat)]
        col_headers = [""] + col_headers
        
        return tabulate(adj_mat_with_row_headers, headers=col_headers, tablefmt="grid")
    
    def add_undirected_edge(self, v1, v2):
        if v1 not in self.adj_list:
            self.adj_list[v1] = set()
        if v2 not in self.adj_list:
            self.adj_list[v2] = set()
        
        self.adj_list[v1].add(v2)
        self.adj_list[v2].add(v1)

    def add_directed_edge(self, v1, v2):
        if v1 not in self.adj_list:
            self.adj_list[v1] = set()
        if v2 not in self.adj_list:
            self.adj_list[v2] = set()
        
        self.adj_list[v1].add(v2)

    def bfs(self, start):
        queue = deque([start])
        visited = set()
        traversal_order = []

        while queue:
            node = queue.popleft()
            if node not in visited:
                visited.add(node)
                traversal_order.append(node)
                for neighbor in self.adj_list[node]:
                    if neighbor not in visited:
                        queue.append(neighbor)
        
        return traversal_order
    
    def dfs(self, start):
        visited = set()
        stack = [start]
        traversal_order = []

        while stack:
            node = stack.pop()
            if node not in visited:
                visited.add(node)
                traversal_order.append(node)
                stack.extend(self.adj_list[node])
        
        return traversal_order

g = Graph()

g.add_undirected_edge(0, 1)
g.add_undirected_edge(0, 2)
g.add_undirected_edge(1, 2)
g.add_undirected_edge(1, 3)
g.add_undirected_edge(2, 4)
g.add_undirected_edge(3, 4)

print(g)

print(f"BFS order: {g.bfs(0)}")
print(f"DFS order: {g.dfs(0)}")
