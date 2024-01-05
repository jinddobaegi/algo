# Boyer Moore
# 패턴의 뒷 부분부터 일치하는지 확인 -> 이야 이거 되게 효율적이다
# 일치하지 않는다? -> 패턴 길이만큼 이동이 핵심

def preprocess(pattern):
    M = len(pattern)
    skip_dict = dict()
    for i in range(M):
        if not skip_dict.get(pattern[M-i-1]):
            skip_dict[pattern[M-i-1]] = i

    return skip_dict


def boyer_moore(target, pattern, skip_dict):
    p_len = len(pattern)
    t_len = len(target)
    p_idx = p_len - 1
    t_idx = p_idx

    i = 0  # 이동한 인덱스 위치 저장
    while t_idx <= t_len:
        if pattern[p_idx] == target[t_idx]:
            p_idx -= 1
            t_idx -= 1
            if p_idx == -1:
                return t_idx + 1
        else:
            p_idx = p_len - 1
            if target[t_idx] in skip_dict.keys():
                i += skip_dict.get(target[i + p_idx])
            else:
                i += p_len
            t_idx = i + p_idx
    return -1


pattern = 'banana'
target = 'baanaaabanaanabananaaaana'

skip_dict = preprocess(pattern)
print(skip_dict)
res = boyer_moore(target, pattern, skip_dict)
print(res)