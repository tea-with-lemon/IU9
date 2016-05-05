n=int(input())
m=int(input())
graph={}
for i in range(n):
    graph[i]=[]
for _ in range(m):
    x, y=map(int, input().split(' '))
    graph[x].append(y)
    graph[y].append(x)
"""print(graph)
b=int(input())
visited=[b]
sosedi=graph[b].copy()
#обход графа в ширину(bfs)
print('bfs')
while sosedi != []:
    i=sosedi.pop(0)
    print(i)
    if i not in visited:
        visited.append(i)
        sosedi=sosedi+graph[i].copy()
print(visited)
#обход графа в глубину
print('dfs')
visited=[b]
sosedi=graph[b].copy()
while sosedi != []:
    i=sosedi.pop()
    print(i)
    if i not in visited:
        visited.append(i)
        sosedi=sosedi+graph[i].copy()
print(visited)"""
#вывод графа
print("strict graph {")
for key, value in graph.items():
    for v in value:
        print(key, '--', v)
print("}")
