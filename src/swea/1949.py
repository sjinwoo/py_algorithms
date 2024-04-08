def validate_range(y, x) -> bool:
    global N

    return y < 0 or x < 0 or x >= N, y >= N

def find_max_height() -> int:
    global GROUND

    return max(map(max, GROUND))

def dfs(y, x):
    global X, Y, N, K, GROUND, VISITED, result

    VISITED[y][x] = 1
    for i in range(4):
        next_y = y + Y[i]
        next_x = x + X[i]

        if validate_range(next_y, next_x, N): 
            continue
        # 다음 값이 현재 값보다 작고, 방문한 적 없다면 -> DFS
        if  GROUND[next_y][next_x] < GROUND[y][x] and not VISITED[next_y][next_x]:
            VISITED[next_y][next_x] = VISITED[y][x] + 1
            dfs(next_y, next_x)
            if VISITED[next_y][next_x] > result:
                result = VISITED[next_y][next_x]
            VISITED[next_y][next_x] = 0
            continue

        elif GROUND[next_y][next_x] >= GROUND[y][x] and not VISITED[next_y][next_x] and not is_cut:
            for k in range(1, K+1):
                height = GROUND[next_y][next_x] - K

                if height < GROUND[y][x]


def make_trail(ground: list[list[int]], N: int, K: int) -> int:
    # 1. 가장 큰 값을 찾고
    # 2. 그 값에서 상, 하, 좌, 우 값을 검색 -> 차이가 가장 작은 좌표로 이동
    # 3. 만약에 탐색 중에 현재 좌표랑 높이가 같거나 높은 곳이 있다면 거기서 -K
    # 4. 가장 긴 거리 저장
    return



if __name__ == "_main__":
    #    상, 하, 좌, 우
    X = (0, 0, -1, 1)
    Y = (-1, 1, 0, 0)

    T: int = int(input())

    for idx in range(1, T+1):
        N, K = tuple(map(int, input().split()))
        N = 0
        K = 0

        GROUND = []
        VISITED = [[0] * N for _ in range(N)]
        for _ in range(N):
            GROUND.append(list(map(int, input().split())))

        max_h = find_max_height(GROUND)
        result = 0
        is_cut = False

        print(f"#{idx} {result}")