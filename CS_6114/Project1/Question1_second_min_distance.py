import sys
def partition(A,start,end):
    pindex = start
    pivot = A[end]
    for i in range(start,end):
        if A[i] <= pivot:

            A[pindex],A[i]=A[i],A[pindex]
            pindex += 1

    A[end], A[pindex] = A[pindex], A[end]
    return pindex

def quicksort(A,start,end):
    if start< end:
        pindex = partition(A,start,end)
        quicksort(A,start,pindex-1)
        quicksort(A,pindex+1,end)
    return A

def solver(arr,n):
    sort_list = quicksort(arr,0,n-1)
    first_min = sys.maxsize
    second_min = sys.maxsize
    f = []
    s = []
    if n <2:
        print('Array does not have enough values')
        return 0
    else:
        for i in range(len(sort_list) - 1):
            diff = abs(sort_list[i] - sort_list[i + 1])
            if diff < first_min:
                second_min = first_min
                s = f
                first_min = diff
                f = [sort_list[i],sort_list[i+1]]
            elif diff < second_min:
                second_min = diff
                s = [sort_list[i], sort_list[i + 1]]
    print('Your output will be redirected to Answer1.txt')
    with open('Answer1.txt','w') as file:
        file.write("Sorted Form of array: " +str(sort_list)+'\n')
        file.write("First Minimum: " + str(f) + ' ' + str(first_min)+'\n')
        file.write("Second Minimum: " + str(s) +' ' + str(second_min))
    return

print('Welcome !! This program prints the sorted Array and then prints the first minimum and ')
print('second minimum difference between any successive elements in its sorted form.')

n = int((input('How many elements are there in your array: ')))
arr =[]
for i in range(int(n)):
    x=int(input("enter each number and press enter. \n"))
    arr.insert(i,x)
    i+=1
solver(arr,n)