score = [39, 59, 62, 67, 70, 78, 83, 85, 88, 92]  
left=0
right=9
x = left + int((59-score[left])/(score[right]-score[left])*(right-left))
print("x為", x) 
while score[x] != 59:
    print("檢查score[", x, "]=", score[x],"是否等於59") 
    if left >=right:
        break         
    if score[x] > 59:
        right = x-1       
    else:
        left = x+1            
    x = left + int((59-score[left])/(score[right]-score[left])*(right-left))
    print("right更新為", right)
    print("left更新為", left)
    print("x更新為", x)   
if score[x] == 59:
    print("找到59分") 
else:
    print("找不到59分")
