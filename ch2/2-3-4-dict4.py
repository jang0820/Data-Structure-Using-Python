lang1={'早安':'Good Morning','你好':'Hello'}
lang2 = lang1
lang2['你好']='Hi'
print('lang1為', lang1)
print('lang2為', lang2)
lang1={'早安':'Good Morning','你好':'Hello'}
lang3 = lang1.copy()
lang3['你好']='Hi'
print('lang1為', lang1)
print('lang3為', lang3)