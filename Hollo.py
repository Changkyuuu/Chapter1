
# 주석입니다.
print('helloworld')

a=1
if(a>1):
    print("어려워")

    if a+1 == 2:
        print("너무 어려워")

print("집에갈래")

def int2digit(n,base):
    res = ""
    while(n>0):
        n,r=divmod(n,base)
        res=str(r)+res
    return res


result = int2digit(22,2)

print(result)
