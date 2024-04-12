def check_connection(curr_path: int, next_tunnel: tuple[int]):
    if curr_path % 2 == 0:
        return (curr_path + 1) in next_tunnel
    else:
        return (curr_path - 1) in next_tunnel

def validate_range(y, x) -> bool:
    global N, M

    return 0 <= y < N and 0 <= x < M

def bfs(r, c):
    global TUNNEL, UNDER_GROUND, N, M, L, MOVE, VISITED

    result = 0
    # 시작점 queue에 넣고 방문할 좌표가 없을 때 까지 반복
    queue = [(r, c)]
    
    while queue != []:
        print(queue)

        # 방문할 좌표 꺼내서 방문했다고 표시
        curr_y, curr_x = queue.pop(0)
        result += 1

        if L > 0:
            # 현재 좌표에서 터널 유형에 따라 상, 하, 좌, 우 순회
            for m in TUNNEL[UNDER_GROUND[curr_y][curr_x]]:
                _X, _Y = MOVE[m]
                next_x = curr_x + _X
                next_y = curr_y + _Y

                # 유효하지 않은 범위나, 연결된 다음 터널이 없다면 pass
                if not validate_range(next_y, next_x) or UNDER_GROUND[next_y][next_x] == 0: 
                    continue
                
                # 방문한적 없고, 다음 좌표가 올바르게 연결된 터널이라면 Queue에 넣어서 다음에 방문하기
                if VISITED[next_y][next_x] == 0 and check_connection(m, TUNNEL[UNDER_GROUND[next_y][next_x]]):
                    VISITED[curr_y][curr_x] = 1
                    queue.append((next_y, next_x))

            L -= 1

    for a in VISITED:
        print(a)

    return result

if __name__ == "__main__":
    TUNNEL = [
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

        VISITED = [[0] * M for _ in range(N)]
        VISITED[R][C] = 1
        result = bfs(R, C)

        result_list.append(result)

    for idx, res in enumerate(result_list, start=1):
        print(f"#{idx} {res}")