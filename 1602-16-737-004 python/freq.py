k = input()
res = dict()
list1 = list(k.split(' '))
for i in list1:
    if(i not in res):
        res[i] = 1
    else:
        res[i] = res[i]+1
print(res)
