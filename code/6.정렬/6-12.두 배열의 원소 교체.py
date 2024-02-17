n,k=map(int,input().split())

a=list(map(int,input().split()))
b=list(map(int,input().split()))

#최악의 경우에도 NlogN을 보장
a.sort() #오름차순
b.sort(reverse = True) #내림차순

cnt=0

for i in range(k): #0~n-1
    if a[i] < b[i]:
        a[i], b[i] = b[i], a[i]
    else: 
        break

print(sum(a))