qu = []
n = int(input())
nums = input().split()
for i in range(n):
    qu.append(nums[i])
while len(qu) > 1:
    x = qu.pop(0)
    print("將", x, "加到最後")
    qu.append(x)
    x = qu.pop(0)
    print("將", x, "加到最後")
    qu.append(x)
    x = qu.pop(0)
    print("將", x, "刪除")
print("剩餘最後一個號碼為", qu[0])


