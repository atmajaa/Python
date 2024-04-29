nums = [1,2,3,4,5]
for num in nums:
    print(num)
#Two most important keywords while working with loops
#1. Break
#2. Continue
#Break - The break keyword will completely break out of the loop
#Scenario - Let's say we are looking for a certain number in our list and after finding that certain number we dont need to continue looping through that list. This is where break comes in usse
for i in range(0,10):
    if i == 5:
        print("Found 5!")
        break
    print(i)

num2 = [45,7,63,96,2]
for nums2 in num2:
    if nums2 == 96:
        print("Found")
        break
    print(nums2)

#To ignore a value but not break out of a loop use the continue keyword. It will skip to the next iteration of the loop
for nums2 in num2:
    if nums2 == 96:
        print("Found")
        continue
    print(nums2)

#Nested loops
for num in nums:
    for letter in 'abc':
        print(num, letter)

#While
x = 0
while x < 10:
    print("Its the same everyday")
    x+=1