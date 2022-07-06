def solution(land):
    # F1 += max(F0) => F1 = [1,2,3,5]
    # F2 += max(F1) => F2  [10,11,12,11]
    # F3 += max(F2) => F3 = [16,15,13,13]
    for i in range(1,len(land)) :
        m_index = land[i-1].index(max(land[i-1]))
        land[i] = [l+land[i-1][m_index] if j != m_index else l+sorted(land[i-1])[-2] for j,l in enumerate(land[i]) ]
    return max(land[-1])
