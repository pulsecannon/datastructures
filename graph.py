"""Defines the graph datastructures."""

import collections
import queue


class Graph(object):

    def __init__(self):
        self._graph = collections.defaultdict(set)

    def add_edge(self, start_node, end_node):
        self._graph[start_node].add(end_node)

    def get_edges(self, src):
      return self._graph[src]

    def dfs(self, src, dst):
        visited = set()
        return self._dfs(src, dst, visited)

    def _dfs(self, src, dst, visited):
      if src in visited:
        return False
      visited.add(src)
      if src == dst:
        return True
      for child in self.get_edges(src):
        if self._dfs(child, dst, visited):
          return True
      return False

    def bfs(self, src, dst):
      visited = set()
      to_visit = queue.Queue()
      to_visit.put(src)
      while not to_visit.empty():
        node = to_visit.get()
        if node == dst:
          return True
        if node in visited:
          continue
        visited.add(node)
        for child in self.get_edges(node):
          to_visit.put(child)
      return False


class AdjMatrix(object):

  def __init__(self, nodes):
    number_of_nodes = len(nodes)
    self._graph = [[0] * number_of_nodes] * number_of_nodes
    self._node_idx = {nodes[i]: i for i in range(number_of_nodes)}

  def 
