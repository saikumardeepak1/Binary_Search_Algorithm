pos = 0
def search(list,n):
    l= 0
    u = len(list)-1
    while l<= u:
        mid = (l+u)//2
        if list[mid] == n:
            globals()['pos']= mid
            return True
        else:
            if list[mid]>n:
                u = mid -1
            else:
                l = mid +1
    return False
list = [1,2,3,4,5,6,7,8,9,11,22,33,44,55,66,77]
n = 44
if search(list,n):
    print("Found at position",pos)
else:
    print("not found")