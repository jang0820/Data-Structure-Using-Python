t1 = ()
print(t1)
t2 = 1, 2 ,3
print(t2)
t3 = (1, 2, 3)
print(t3)
print(t3[0])
t3 = (1, 2, 3)
a, b, c= t3
print('a=', a, ',b=', b, ',c=', c)
a = 10
b = 20
print('交換前','a=', a, ',b=', b)
a, b = b, a
print('交換後','a=', a, ',b=', b)
list1=[1,2,3,4]
t4 = tuple(list1)
print(t4)
t4 = (1,2,3,4)
t5 = (t4,5,6)
print(t5)
print(len(t5))
print(t5[0][0])
t6 = ('z', )
print(t6)