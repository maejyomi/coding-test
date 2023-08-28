from collections import deque

def word_conversion(begin, target, words):
    # 초기화
    queue = deque()
    queue.append([begin, 0])
    visited = [0] * len(words)
    cnt = 0

    # 계산
    while queue:
        word, cnt = queue.popleft()
        if word==target: return cnt
        for i in range(len(words)):
            if not visited[i]:
                if sum(x!=y for x, y in zip(word,words[i])) == 1: # 두 문자를 비교해서 한 문자만 변경되어 있는 것
                    queue.append([words[i], cnt+1])
                    visited[i] = 1
    # 결과
    return 0
    