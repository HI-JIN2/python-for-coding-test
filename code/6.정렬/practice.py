n=int(input())

array=[]

for i in range(n):
    # input_data= input().split()
    # array.append((int(input_data[0]), int(input_data[1])))
    [a,b] = map(int, input().split())
    array.append([a,b])

array = sorted(array)

for i in range(n):
    print(array[i][0],array[i][1])
