# 순열: 순서가 있고, 중복 허용 X

def permutation(n, new_list):
    # 중단 조건
    if len(new_list) == n:
        print(new_list)
        return
