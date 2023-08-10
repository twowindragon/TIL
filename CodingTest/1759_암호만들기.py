def dfs(vowel_cnt, consonant_cnt, ans):
    if len(ans) == L and vowel_cnt >= 1 and consonant_cnt >= 2:
        print(ans)
        return
    for i in range(C):
        if ans and ans[-1] >= seq[i]:
            continue
        if seq[i] in vowel:    
            dfs(vowel_cnt + 1, consonant_cnt, ans + seq[i])
        else:
            dfs(vowel_cnt, consonant_cnt + 1, ans + seq[i])
        
L, C = map(int, input().split())
seq = sorted(list(input().split()))

vowel = {'a', 'e', 'i', 'o', 'u'}
dfs(0, 0, '')
