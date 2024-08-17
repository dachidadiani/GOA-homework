def smaller(arr):
    result = []
    count = 0
    for i in range(len(arr)):
        
        for j in range(i + 1, len(arr)):
           
            if arr[i] > arr[j]:
               
                count += 1
        result.append(count)
        
        count = 0
        
    return result
 

print(smaller([5,4,3,2,1]))