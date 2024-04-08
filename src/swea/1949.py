#    상, 하, 좌, 우
X = (0, 0, -1, 1)
Y = (-1, 1, 0, 0)

def validate_range(y, x, N) -> bool:
    return y < 0 or x < 0 or x >= N, y >= N

def find_max_height(ground: list[list[int]]) -> int:
    return max(map(max, ground))

def dfs(ground: list[list[int]], visited: list[list[bool]], y, x, N):
    global X, Y
    visited[y][x] = 1
    for i in range(4):
        next_y = y + Y[i]
        next_x = x + X[i]
        if validate_range(next_y, next_x, N): continue
        elif


def make_trail(ground: list[list[int]], N: int, K: int) -> int:
    # 1. 가장 큰 값을 찾고
    # 2. 그 값에서 상, 하, 좌, 우 값을 검색 -> 차이가 가장 작은 좌표로 이동
    # 3. 만약에 탐색 중에 현재 좌표랑 높이가 같거나 높은 곳이 있다면 거기서 -K
    # 4. 가장 긴 거리 저장
    Q = deque()
    return length_trail



if __name__ == "_main__":
    T: int = int(input())

    for IDX_TEST_CASE in range(1, T+1):
        ground = list()
        N, K = tuple(map(int, input().split()))
        for _ in range(N):
            ground.append(list(map(int, input().split())))

        visited = [[False] * N for _ in range(N)]
        max_h = find_max_height(ground)
        result = make_trail(ground, visited, N, K)

        print(f"#{IDX_TEST_CASE} {result}")