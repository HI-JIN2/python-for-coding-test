n=int(input())
n_array =[]
for i in range(n):
    n_array.append(list(map(int,input().split())))


m=int(input())
m_array =[]
for i in range(m):
    m_array.append(list(map(int,input().split())))

cnt=[0]*len(m_array)
for i in n_array:
    for j in m_array:
        if n_array[i] == m_array[j]:
            cnt[m_array[j]]+=1

print(cnt)