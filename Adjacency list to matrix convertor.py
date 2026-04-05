def adjacency_list_to_matrix(adj_list):
    n = len(adj_list)

    matrix = [[0 for _ in range(n)] for _ in range(n)]

    for node in adj_list:
        for neighbor in adj_list[node]:
            matrix[node][neighbor] = 1

    for row in matrix:
        print(row)

    return matrix

print(adjacency_list_to_matrix({0: [2], 1: [2, 3], 2: [0, 1, 3], 3: [1, 2]}))