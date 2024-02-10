#swap two elements by position
def swap(a,b,arr):
    arr[a],arr[b] = arr[b],arr[a]
    print(arr)

n = int(input("Enter the size : ")) 
arr =[]
for i in range(n):
    while True:
        try:
            element = int(input("Enter the element : "))
            arr.append(element)
            break;
        except Exception as e:
            print(e)

a = int(input("Enter the postion of 1st element : "))
b = int(input("Enter the postion of 2nd element : "))

swap(a,b,arr)
