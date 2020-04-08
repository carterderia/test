
# 方法1 非函數式編程
s = 0
for x in range(1, 10):
    s += x ** 2
print(s)

# 方法2 me 
# def mypow(x):
#     return x ** 3
# l = []
# for x in map(mypow, range(1, 10)):
#     l.append(x)
# print(l)   # x=2 -> [1, 4, 9, 16, 25, 36, 49, 64, 81] , 和為： 285
# print('和為：', sum(l)) # x=3 -> [1, 8, 27, 64, 125, 216, 343, 512, 729] , 和為：2025

# 方法3 老師
def pow2(x):
    return x ** 2
print(sum(map(pow2, range(1,10))))   

# 方法4 
print(sum(map(lambda x: x ** 2, range(1,10)))) 

# me
# def mypow2(x, y):
#     return x ** y
# L = []
# for x in map(mypow2, range(1, 10), range(9, 0, -1)):
#     L.append(x)
# print(L) # [1, 256, 2187, 4096, 3125, 1296, 343, 64, 9]
# print(sum(L)) # 11377

def pow3(x, y):
    return x ** y
print(sum(map(pow3, range(1, 10), range(9, 0, -1))))
print(map(pow3, range(1, 10), range(9, 0, -1)))

print(sum(map(pow, range(1, 10), range(9, 0, -1))))

# 計算 1 + 2**3 + 3**3 + 4**3 + .... + n**3 的和
print(sum(map(lambda x: x**3, range(1, 5+1))))
# 計算 1 + 2**2 + 3**3 + 4**4 + .... + n**n 的和
print(sum(map(pow, range(1, 4+1), range(1, 4+1))))
print(sum(map(lambda x: x**x, range(1, 4+1))))

# 階層, 4! = 4*3*2*1 = 24
def mylel(x):
    if x == 1: # 設置遞歸終點
        return 1
    return x * mylel(x-1)      

print(mylel(5))

