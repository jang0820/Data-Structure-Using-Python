dict1={}
print(dict1)
lang={'早安':'Good Morning', '你好':'Hello'}
print(lang)
lang={'早安':'Good Morning', '你好':'Hello'}
print('「你好」的英文為',lang['你好'])
lang={'早安':'Good Morning', '你好':'Hello'}
#print('「你好嗎」的英文為',lang['你好嗎'])
lang={'早安':'Good Morning', '你好':'Hello'}
print('「你好」的英文為',lang.get('你好'))
print('「你好嗎」的英文為',lang.get('你好嗎'))
print('「你好嗎」的英文為',lang.get('你好嗎','不在字典內'))
lang={'早安':'Good Morning', '你好':'Hello'}
lang['你好']='Hi'
print(lang)
lang['學生']='Student'
print(lang)
lang={'早安':'Good Morning', '你好':'Hello'}
del lang['早安']
print(lang)
lang={'早安':'Good Morning', '你好':'Hello'}
lang.clear()
print(lang)
