字典 = {'dog':'狗', 'fish':'魚', 'cat':'貓', 'pig':'豬'}
print(字典.keys())
print(字典)
英文 = input('請輸入一個英文單字？')
print(字典.get(英文,'字典找不到該單字'))
