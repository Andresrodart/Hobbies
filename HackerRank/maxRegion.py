import math
import os
import random
import re
import sys

# Complete the maxRegion function below.
def maxRegion(grid):
  res, node_count = -1, 1
  graph = []
  for i in range(len(grid)):
    for j in range(len(grid[i])):
      if grid[i][j] == 1: 
        grid[i][j] = node_count
        node_count += 1
  for i in range(node_count): graph.append([])  
  visited = [False] * node_count
  for i in range(len(grid)):
    for j in range(len(grid[i])):
      if grid[i][j] != 0: 
        if i - 1 >= 0 and j - 1 >= 0 and grid[i - 1][j - 1] != 0: graph[grid[i][j]].append(grid[i - 1][j - 1])
        if i - 1 >= 0 and grid[i - 1][j] != 0: graph[grid[i][j]].append(grid[i - 1][j])
        if i - 1 >= 0 and j + 1 < len(grid[i]) and grid[i - 1][j + 1] != 0: graph[grid[i][j]].append(grid[i - 1][j + 1])
        if j - 1 >= 0 and grid[i][j - 1] != 0: graph[grid[i][j]].append(grid[i][j - 1])
        if j + 1 < len(grid[i]) and grid[i][j + 1] != 0: graph[grid[i][j]].append(grid[i][j + 1])
        if i + 1 < len(grid) and j - 1 >= 0 and grid[i + 1][j - 1] != 0: graph[grid[i][j]].append(grid[i + 1][j - 1])
        if i + 1 < len(grid) and grid[i + 1][j] != 0: graph[grid[i][j]].append(grid[i + 1][j])
        if i + 1 < len(grid) and j + 1 < len(grid[i]) and grid[i + 1][j + 1] != 0: graph[grid[i][j]].append(grid[i + 1][j + 1])
  print(graph)
  for i in range(1, node_count):
    if not visited[i]: res = max(res, dfs(i, graph, visited))
  return res
def dfs(root, graph, visited):
  queue = [root]
  res = 0
  while queue:
    parent = queue.pop(0)
    if not visited[parent]:
      visited[parent] = True
      res += 1
      for child in graph[parent]: queue.append(child)
  return res
if __name__ == '__main__':
    n = int(input())
    m = int(input())
    grid = []
    for _ in range(n):
        grid.append(list(map(int, input().rstrip().split())))
    res = maxRegion(grid)
    print(res)