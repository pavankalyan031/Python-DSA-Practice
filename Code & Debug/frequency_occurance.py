#brute force

num=[1,2,3,4,5,6,6,77,8,7,8]
freq_map={} #dict()
for i in range(0, len(num)):
    if num[i] in freq_map:
        freq_map[num[i]]+=1
    else:
        freq_map[num[i]]=1
print(freq_map)

#time complexity= O(n) if use the nested loop without the frequency map the O(n*2)
#space complexity = O(1) its taking the constant time to updating the count 



#method 2 (optimal solution)
num=[1,2,3,4,5,6,6,77,8,7,8]
n=len(num)
hash_map=dict()
for i in range(0, n):
    hash_map[num[i]]= hash_map.get(num[i],0)+1
    
print(hash_map)

