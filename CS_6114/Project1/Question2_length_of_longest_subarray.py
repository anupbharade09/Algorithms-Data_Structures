# partition function by taking pivot element in quick sort
def partition(A, start, end):
    pindex = start
    pivot = A[end]
    for i in range(start, end):
        if A[i] <= pivot:
            A[pindex], A[i] = A[i], A[pindex]
            pindex += 1

    A[end], A[pindex] = A[pindex], A[end]
    return pindex

# Main quicksort function
def quicksort(A, start, end):
    if start < end:
        pindex = partition(A, start, end)
        quicksort(A, start, pindex - 1)
        quicksort(A, pindex + 1, end)
    return A

# Solver function
def solver(arr, n, x):
    # redirecting output to a file
    print('Your output will be redirected to Answer2.txt')
    with open('Answer2.txt', 'w') as file:
        # sort array and store it
        sort_arr = quicksort(arr, 0, n - 1)
        # Find the index of given x or nearest greater element of x
        for i in range(n):
            if sort_arr[i] == x:
                index = i
                break
            elif sort_arr[i] > x:
                index = i
                break
        # left is left part of array from x and right is right part from x
        left = len(sort_arr[:index])
        right = len(sort_arr[index:]) - 1

        # If found index equals to x then print length of subarray based on elements on left and right side
        if sort_arr[index] == x:
            if left <= right:
                file.write('Length of the longest subarray: '+ str(len(sort_arr)))
            else:
                file.write('Length of the longest subarray: '+ str((right * 2) + 1))
        else:
            # condition to check if found index is not on 0th position
            if index > 0:
                # Condition to check if found average of index and previous index element is lesser than x
                if ((sort_arr[index - 1] + sort_arr[index]) / 2) < x:
                    if left <= right:
                        file.write('Length of the longest subarray: '+ str(len(sort_arr)))
                    else:
                        file.write('Length of the longest subarray: ' + str((right * 2) + 1))
                else:
                    if left <= right:
                        file.write('Length of the longest subarray: '+ str(len(sort_arr)))
                    else:
                        file.write('Length of the longest subarray: ' + str((right * 2) + 2))
            # condition to check if found index is not at 0th position then directly print length of array
            else:
                file.write('Length of the longest subarray: '+ str(len(sort_arr)))
    return

print('Welcome !! This program finds the length of longest subarray')

n = int((input('How many elements are there in your array: ')))
x = int((input('Enter the value of x : ')))
arr = []
for i in range(int(n)):
    temp = int(input("enter each number and press enter. \n"))
    arr.insert(i, temp)
    i += 1
# call to solver function
solver(arr, n, x)