import math
import os
import random
import re
import sys

# Complete the findShortest function below.

#
# For the weighted graph, <name>:
#
# 1. The number of nodes is <name>_nodes.
# 2. The number of edges is <name>_edges.
# 3. An edge exists between <name>_from[i] to <name>_to[i].
#
#
def findShortest(graph_nodes, graph_from, graph_to, ids, val):
    shortest = sys.maxsize
    graph = to_graph(graph_from, graph_to, graph_nodes)
    count, shortest = 0, sys.maxsize
    for i in range(graph_nodes):
      if ids[i] == val: count += 1
    if count <= 1: return -1
    for i in range(graph_nodes):
      if ids[i] == val: shortest = min(shortest, BFS(i, val, ids, graph))
      print('ss', shortest)
    return shortest

def BFS(root, target, ids, graph):
  visited = [False] * len(graph)
  queue = [[root, 0]]
  while queue:
    parent = queue.pop(0)
    if not visited[parent[0]]:
      visited[parent[0]] = True
      if parent[1] > 0 and ids[parent[0]] == target: return parent[1]
      for child in graph[parent[0]]: queue.append([child, parent[1] + 1])
  return sys.maxsize

def to_graph(from_, to_, n):
  graph = [[] for _ in range(n)]
  for i in range(len(from_)): 
  	graph[from_[i] - 1].append(to_[i] - 1)
  	graph[to_[i] - 1].append(from_[i] - 1)
  return graph
if __name__ == '__main__':
  graph_nodes, graph_edges = map(int, input().split())
  graph_from = [0] * graph_edges
  graph_to = [0] * graph_edges
  for i in range(graph_edges):
      graph_from[i], graph_to[i] = map(int, input().split())
  ids = list(map(int, input().rstrip().split()))
  val = int(input())
  ans = findShortest(graph_nodes, graph_from, graph_to, ids, val)
  print(ans)