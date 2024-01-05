# Brute Force
# i랑 p랑 한 자리 씩 비교해보면서
# 일치하지 않으면 t += 1, p = 0
# 일치하면 t랑 p랑 다음 자리를 확인
# 찾거나 t가 끝까지 가면 종료

def my_func(target, pattern):
    t = 0
    p = 0
    while t < len(target) and p < len(pattern):
        if target[t] == pattern[p]:
            t += 1
            p += 1
        else:
            t -= p-1
            p = 0

    if p == len(pattern):
        return f'{t - p}번째 idx에 패턴 시작~'
    else:
        return '응 없쩡'


res = my_func('patternmatching', 'match')
print(f'브루트 포스 패턴매칭 결과: {res}')