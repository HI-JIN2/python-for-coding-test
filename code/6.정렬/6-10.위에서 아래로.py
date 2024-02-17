n=int(input())

array=[]

for i in range(n):
    # a=int(input())
    # array.append(a)
    array.append(int(input())) #이렇게 바로 받을 수 있음

array.sort(reverse=True)
#또는
#array=array.sorted(array, reverse=True)

for i in array:
    print(i,end=" ")
