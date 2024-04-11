def validate_range(y, x) -> bool:
    global N, M

    return 0 <= y < N and 0 <= x < M

def dfs(y, x):
    global UNDER_GROUND, N, M, R, C, L, MOVE, VISITED, result
    if L == 1:
        return
    
    
    L -= 1
    for m in PATH[UNDER_GROUND[y][x]]:
        _X, _Y = MOVE[m]
        next_x = x + _X
        next_y = y + _Y

        if not validate_range(next_y, next_x): 
            continue

        if VISITED[next_y][next_x] == 0:
            result += 1
            VISITED[next_y][next_x] = 1
            dfs(next_y, next_x)


if __name__ == "__main__":
    PATH = [
        (),
        (0, 1, 2, 3), 
        (0, 1), 
        (2, 3),
        (0, 3), 
        (1, 3), 
        (1, 2),
        (0, 2)
    ]
    #         상       하       좌      우
    MOVE = [(0, -1), (0, 1), (-1, 0), (1, 0)]


    T = int(input())

    result_list = []
    for idx in range(1, T+1):
        N, M, R, C, L = map(int, input().split())

        UNDER_GROUND = []
        for _ in range(N):
            UNDER_GROUND.append(list(map(int, input().split())))

        VISITED = [[0] * N for _ in range(N)]
        result = 0
        VISITED[R][C] = 1
        dfs(R, C)
        result_list.append(result)

    for idx, res in enumerate(result_list, start=1):
        print(f"#{idx} {res}")