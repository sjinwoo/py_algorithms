from collections import deque

# 격자 원소 수: N x N
N = 10

#    상, 하, 좌, 우
dx = (0, 0, -1, 1)
dy = (-1, 1, 0, 0)

def validate_range(y, x):
    return x < 0 or y < 0 or x >= N or y >= N


def bfs(x, y):
    Q = deque()

    # 시작 좌표 삽입, visited 표시
    Q.append((y, x))
    visited = [[False] * N for _ in range(N)]
    visited[y][x] = True

    while Q:
        curr_y, curr_x = Q.popleft()
        # Left Pop 한 원소의 상, 하, 좌, 우 탐색
        for d in range(4):
            new_y = curr_y + dy[d]
            new_x = curr_x + dx[d]

            # 이미 방문했거나, 범위 밖인 경우
            if validate_range(new_y, new_x) or visited[new_y][new_x]: 
                continue
            else:
                # 이후 동작 호출
                # 탐색한 좌표 추가
                Q.append((new_y, new_x))
                visited[new_y][new_x] = True