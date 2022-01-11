import random
import time
nums = []
for i in range(1000000):
    nums.append(random.uniform(1,10))
start = time.time()
nums.sort()
end = time.time()
print("排序花費",end-start,"秒")

