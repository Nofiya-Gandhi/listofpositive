#input numbers

inputlist = input("Enter numbers saperated by space:") 
list1=inputlist.split()
list2=[]
for element in list1:
    if int(element) > 0:
        list2.append(int(element))
        
print("\nlist of positive numbers: \n") 
print(list2)
