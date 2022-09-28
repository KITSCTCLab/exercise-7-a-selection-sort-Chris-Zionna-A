from typing import List

def selectionSort(array, size) -> List[int]:
  for i in range(size-1):
    m=array[i]
    p=i
    for j in range (i, size):
    
      if array[i]>array[j]:
        m=array[j]
        p=j
    temp=array[i]
    array[i]=array[j]
    array[j]=temp
        
        
# Do not change the following code
input_data = input()
data = []
for item in input_data.split(', '):
  if item.isnumeric():
    data.append(int(item))
  elif item.lstrip("-").isnumeric():
    data.append(int(item))
print(selectionSort(data, len(data)))
