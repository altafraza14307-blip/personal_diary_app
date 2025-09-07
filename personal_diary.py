def odd_num_addition(list):
    add = 0
    for i in list:
        if i%2!=0:
            add+=1
        return add
list = [12,3,7,8]
res = odd_num_addition(list)  
print(res)