#Find addition of all the odd numbers from 1 to 20. That is, 
#find addition of numbers 1, 3, 5 …19.

add=0
count=1
while count<20:
    if count%2!=0:
        add=add+count
    count+=1
print("***addition of all the odd numbers from 1 to 20 is****")
print(add)