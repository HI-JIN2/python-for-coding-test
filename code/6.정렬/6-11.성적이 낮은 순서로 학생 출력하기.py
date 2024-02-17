# n=int(input())

# array_a=[]
# array_b=[]
# for i in range(n):
#     a,b = map(str,input().split())
#     array_a.append(a)
#     array_b.append(int(b))

# b_sort= array_b.sort()
# print(b_sort)

# for i in range(n):
#     print(array_a[b_sort[i]])


n=int(input())
array = [ ]
for i in range(n):
    input_data= input().split()
    array.append((input_data[0], int(input_data[1])))

array = sorted(array, key= lambda student: student[1])

for student in array:
    print(student[0], end=" ")