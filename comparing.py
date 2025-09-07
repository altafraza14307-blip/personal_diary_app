def compare_point(a,b):
    alice = 0
    bob = 0
    for i in range(3):
        if a[i]>b[i]:
            alice +=1
        else :
            bob +=1    
    return [alice,bob]
print(compare_point([5,7,3],[2,5,6]))

     
    


