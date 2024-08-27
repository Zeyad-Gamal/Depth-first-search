graph = {
    'P': ['Q','R','S'],
    'Q': ['R'],
    'R': ['T'],
    'S': [],
    'T': []
}

visited = set()
def dfs(visited, graph, node):
  if node not in visited:
    print(node)
    visited.add(node)
    for neighbour in graph[node]:
      dfs(visited, graph, neighbour)


print('Here is the depth first: ')
dfs(visited, graph, 'P')