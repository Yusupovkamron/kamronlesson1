data = [1, 2, 4, 6, 7, 8, 9, 10]
target = int(input('son kiriting '))
data.sort()
l = len(data)-1
low = 0
p = 0
while True:

    middle = (low+l)//2
    p+=1
    if data[middle]==target:
        print(data[middle])
        break
    elif data[middle]>target:
        l = middle-1
    elif data[middle]<target:
        low = middle+1
print(p)