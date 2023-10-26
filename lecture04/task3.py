import random
input_array = list(map(lambda x: int(x), (input("Enter some integers: ")).split()))

while True:
    a = []
    for i in range(1,len(input_array)):
        if input_array[i]>=input_array[i-1]: a.append(1)
        else: a.append(0)
    
    if all(a): break
    else: random.shuffle(input_array)
print(input_array)