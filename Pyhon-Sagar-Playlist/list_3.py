# common elements 
# l_1=[1,2,3,4,5]
#l_2= [1,4,5,6,7]
#common l_3=[1,4,5]


def common():
    l_1=[1,2,3,4,5,6]
    l_2=[1,4,5,4,8,9]
    
    # l_3=list(set(l_1) & set(l_2))
    
    # print(l_3)
    
    
    l_3= list(set(l_1).intersection(set(l_2)))
    print(l_3)
common()
    
    

    