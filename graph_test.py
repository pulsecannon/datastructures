"""Tests the graph test."""

import unittest
import graph


class GraphTest(unittest.TestCase):

  def test_add_edge(self):
    g = graph.Graph()
    g.add_edge('A', 'B')
    g.add_edge('A', 'C')
    g.add_edge('A', 'D')
    self.assertEqual(g.get_edges('A'), {'B', 'C', 'D'})

  def test_dfs(self):
    g = graph.Graph()
    g.add_edge('A', 'B')
    g.add_edge('B', 'C')
    g.add_edge('C', 'D')
    g.add_edge('B', 'E')
    g.add_edge('E', 'F')
    g.add_edge('F', 'D')
    g.add_edge('A', 'C')
    g.add_edge('A', 'F')
    g.add_edge('X', 'Y')
    self.assertTrue(g.dfs('A', 'E'))
    self.assertTrue(g.dfs('A', 'D'))
    self.assertFalse(g.dfs('A', 'X'))
    self.assertFalse(g.dfs('A', 'Y'))

  def test_bfs(self):
    g = graph.Graph()
    g.add_edge('A', 'B')
    g.add_edge('B', 'C')
    g.add_edge('C', 'D')
    g.add_edge('B', 'E')
    g.add_edge('E', 'F')
    g.add_edge('F', 'D')
    g.add_edge('A', 'C')
    g.add_edge('A', 'F')
    g.add_edge('X', 'Y')
    self.assertTrue(g.bfs('A', 'E'))
    self.assertTrue(g.bfs('A', 'F'))
    self.assertFalse(g.bfs('A', 'X'))
    self.assertFalse(g.bfs('A', 'Y'))


if __name__ == '__main__':
    unittest.main()
