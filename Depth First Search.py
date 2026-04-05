def dfs(matrix, start):
    n = len(matrix)
    visited = [False] * n
    stack = [start]
    result = []

    while stack:
        node = stack.pop()

        if not visited[node]:
            visited[node] = True
            result.append(node)

            # Add neighbors to stack
            for neighbor in range(n):
                if matrix[node][neighbor] == 1 and not visited[neighbor]:
                    stack.append(neighbor)

    return result