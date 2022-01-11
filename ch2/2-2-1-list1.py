shoplist = ['牛奶', '蛋', '咖啡豆', '西瓜', '鳳梨']
print('購物清單shoplist為')
print(shoplist)
shoplist = ['牛奶', '蛋', '咖啡豆', '西瓜', '鳳梨']
print('顯示shoplist[0]為',shoplist[0])
shoplist = ['牛奶', '蛋', '咖啡豆', '西瓜', '鳳梨']
print('購物清單shoplist的長度為', len(shoplist))
shoplist = ['牛奶', '蛋', '咖啡豆', '西瓜', '鳳梨']
shoplist[1] = '皮蛋'
print("執行 shoplist[1] = '皮蛋' 後")
print(shoplist)
shoplist = ['牛奶', '蛋', '咖啡豆', '西瓜', '鳳梨']
index=shoplist.index('咖啡豆')
print("執行 index=shoplist.index('咖啡豆') 後")
print('index=', index)
shoplist = ['牛奶', '蛋', '咖啡豆', '西瓜', '鳳梨']
shoplist.append('麵包')
print("執行 shoplist.append('麵包')後")
print(shoplist)
shoplist = ['牛奶', '蛋', '咖啡豆', '西瓜', '鳳梨']
shoplist.insert(4, '蘋果')
print("執行 shoplist.insert(4, '蘋果') 後")
print(shoplist)
shoplist = ['牛奶', '蛋', '咖啡豆', '西瓜', '鳳梨']
shoplist.remove('蛋')
print("執行 shoplist.remove('蛋') 後")
print(shoplist)
shoplist = ['牛奶', '蛋', '咖啡豆', '西瓜', '鳳梨']
del shoplist[0]
print("執行 del shoplist[0] 後")
print(shoplist)
shoplist = ['牛奶', '蛋', '咖啡豆', '西瓜', '鳳梨']
shoplist.pop(0)
print("執行 shoplist.pop(0) 後")
print(shoplist)
shoplist.pop()
print("執行 shoplist.pop() 後")
print(shoplist)
shoplist.pop(-1)
print("執行 shoplist.pop(-1) 後")
print(shoplist)
shoplist = ['milk', 'egg', 'coffee', 'watermelon']
shoplist.sort()
print("執行 shoplist.sort() 後")
print(shoplist)
list = [1,2.0,3,'Python']
print("串列可以包含各種資料型別的元素")
print(list)
shoplist = ['milk', 'egg', 'coffee', 'watermelon']
for item in shoplist:
    print(item)
