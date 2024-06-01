import numpy as np

li = [[1, 2], [2, 3]]

mid_index = len(li) // 2

li2 = li[mid_index:]
li = li[:mid_index]

li = np.array(li)


print(li)
print(li2)