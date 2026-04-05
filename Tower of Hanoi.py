def hanoi_solver(n):
    source = list(range(n, 0, -1))
    auxiliary = []
    target = []

    moves = []
    def record():
        moves.append(f"{source} {auxiliary} {target}")

    def solve(num, src, aux, tgt):
        if num == 1:
            tgt.append(src.pop())
            record()
            return
        
        solve(num - 1, src, tgt, aux)
        tgt.append(src.pop())
        record()
        solve(num - 1, aux, src, tgt)

    record()

    solve(n, source, auxiliary, target)

    return "\n".join(moves)

print(hanoi_solver(4))
