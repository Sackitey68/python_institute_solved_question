blocks = int(input("Enter the number of blocks: "))

#
# Write your code here.
height = 0

while blocks > height:
    height = height + 1 
    blocks = blocks - height
   

print("The height of the pyramid:", height)
