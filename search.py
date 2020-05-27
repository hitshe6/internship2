def binarySearch (arr, l, r, x): 
   
    if r >= l: 
  
        mid = l + (r - l) // 2
        if arr[mid] == x: 
            return mid 
        elif arr[mid] > x: 
            return binarySearch(arr, l, mid-1, x) 
 
        else: 
            return binarySearch(arr, mid + 1, r, x) 
  
    else: 
       
        return -1
L = []
Y= int(input("Enter the No of elements:"))
for j in range (0, Y): 
	ele=int(input("Enter element"))
	L.append(ele)

print(sorted(L))


arr = sorted(L) 

x = int(input("Which element to search First:"))   


result = binarySearch(arr, 0, len(arr)-1, x) 
  
if result != -1: 
    print ("Element is present at index % d" % result) 
else: 
    print ("Element is not present in array")
