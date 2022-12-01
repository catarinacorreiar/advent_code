
list = open("input.txt", "r")
list = list.readlines()
newlist = [] #sum each one

i = 0
elfo = 0  
while i < len(list):

    if list[i] != "\n": 
        elfo += int(list[i])
    else:
        newlist.append(elfo)
        elfo = 0
    i = i + 1
    
        
print("Largest element is:", max(newlist))

sortedlist = sorted(newlist)
print(sortedlist)

sumbigelfo = sortedlist[-1] + sortedlist[-2] + sortedlist[-3]

print(sumbigelfo)