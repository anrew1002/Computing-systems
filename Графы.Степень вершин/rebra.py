with open("input_BIG.txt", "r") as f:
    N, E = list(map(int, f.readline().split()))
    list_of_edges = []
    for edge in f.readlines():
        list_of_edges.append(list(map(int, edge.split())))
list_of_vector_weight = [0 for x in range(N)]
for edge in list_of_edges:
    list_of_vector_weight[edge[0]-1] += 1
    list_of_vector_weight[edge[1]-1] += 1
with open("result.txt", 'w') as f:
    list_of_vector_weight = [str(x) for x in list_of_vector_weight]
    f.write("\n".join(list_of_vector_weight))
