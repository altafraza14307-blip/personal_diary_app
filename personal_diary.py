def odd_num_addition(arr):
    add = 0
    for i in arr:
        if i%2!=0:
            add+=i
    return add
list = [12,3,7,8]
res = odd_num_addition(list)  
print(res)