# step 1 - create an empty list named beatles
beatles = []
print("Step 1:", beatles)

# step 2 - use the append() method to add the following members of the band to the list: John Lennon, Paul McCartney, and George Harrison
beatles.append("John Lennon")
beatles.append("Paul McCartney")
beatles.append("George Harrison")
print("Step 2:", beatles)

# step 3 - use the for loop and the append() method to prompt the user to add the following members of the band to the list: Stu Sutcliffe, and Pete Best
for brand in range(2):
    beatles.append(input("Addd the name of the singer: "))
print("Step 3:", beatles)

# step 4 - use the del instruction to remove Stu Sutcliffe and Pete Best from the list;
# i can use double del instructions
# del beatles[-1]
# del beatles[-1]
# i can also use the for loop
for i in range(2):
    del beatles[-1]
print("Step 4:", beatles)

# step 5 - use the insert() method to add Ringo Starr to the beginning of the list.
beatles.insert(0, "Ringo Starr")
print("Step 5:", beatles)

# testing list length
print("The Fab", len(beatles))
