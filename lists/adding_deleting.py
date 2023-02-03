l1=[23,45,67,12,34]
l1.append(1234)
print(l1)
l1.insert(2,34)
print(l1)
for i in l1:
    print(i)

for j in range(len(l1)):
    print(l1[j])

l1.sort(reverse=True)
print(l1)
