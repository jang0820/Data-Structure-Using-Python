lang={'早安':'Good Morning','你好':'Hello'}
for ch, en in lang.items():
    print('中文為', ch, '英文為', en)
for ch in lang.keys():
    print(ch,lang[ch])
for en in lang.values():
    print(en)