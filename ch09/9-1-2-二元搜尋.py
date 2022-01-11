score = [45, 59, 62, 67, 70, 78, 83, 85, 88, 92]  
mid=5
left=0
right=9
while score[mid] != 59:
    print("檢查score[", mid, "]=", score[mid],"是否等於59") 
    if left >=right:
        break         
    if score[mid] > 59:
        right=mid-1       
    else:
        left=mid+1             
    mid=(left+right)//2
    print("right更新為", right)
    print("left更新為", left)
    print("mid更新為", mid)   
if score[mid] == 59:
    print("找到59分") 
else:
    print("找不到59分") 
