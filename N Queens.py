def dfs_n_queens(n):
    if n < 1:
        return []

    solutions = []

    def is_safe(path, row, col):
        for r in range(row):
            c = path[r]
            # same column or diagonal
            if c == col or abs(c - col) == abs(r - row):
                return False
        return True

    def dfs(row, path):
        if row == n:
            solutions.append(path[:])  # copy solution
            return

        for col in range(n):
            if is_safe(path, row, col):
                path.append(col)
                dfs(row + 1, path)
                path.pop()  # backtrack

    dfs(0, [])
    return solutions