#find the second largest number in a list : 
# list_1=[1,2,3,4,6,89, 90, 90273,3,223]

list_1=[1,2,3,4,6,89, 90, 90273,3,223]
order= sorted(list_1)
print(order)
print(f"Second largest num:", order[-2])
print(list_1)

#using sort.()
list_1=[1,2,3,4,6,89, 90, 90273,3,223]
list_1.sort()
print(list_1[-2])

#unique element remove and give sort
#unique_sorted= sorted(set(list_1))
#print(unique_sorted[-2])

#time complexity is = O(nlogn)

