# Initialize the list my_list with the values [8, 10, 6, 2, 4].
my_list = [8, 10, 6, 2, 4]

# Set the variable swapped to True to enter the while loop.
swapped = True

while swapped:
        # Inside the while loop, set swapped to False to assume that the list is already sorted unless a swap occurs
            swapped = False

                # Use a for loop to iterate over the range from 0 to the length of my_list minus 1.
                    for i in range(len(my_list) - 1):

                                # Check if the current element at index i is greater than the next element at index i + 1.
                                        if my_list[i] > my_list[i + 1]:
                                                       
                                                        # If the condition is true, swap the elements by utilizing a simultaneous assignment.
                                                                    swapped = True
                                                                                
                                                                                            # Set swapped to True since a swap occurred, indicating that the list is not yet fully sorted
                                                                                                        my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]

                                                                                                        print(my_list)# Initialize the list my_list with the values [8, 10, 6, 2, 4].
                                                                                                        my_list = [8, 10, 6, 2, 4]

                                                                                                        # Set the variable swapped to True to enter the while loop.
                                                                                                        swapped = True

                                                                                                        while swapped:
                                                                                                                # Inside the while loop, set swapped to False to assume that the list is already sorted unless a swap occurs
                                                                                                                    swapped = False

                                                                                                                        # Use a for loop to iterate over the range from 0 to the length of my_list minus 1.
                                                                                                                            for i in range(len(my_list) - 1):

                                                                                                                                        # Check if the current element at index i is greater than the next element at index i + 1.
                                                                                                                                                if my_list[i] > my_list[i + 1]:
                                                                                                                                                               
                                                                                                                                                                # If the condition is true, swap the elements by utilizing a simultaneous assignment.
                                                                                                                                                                            swapped = True
                                                                                                                                                                                        
                                                                                                                                                                                                    # Set swapped to True since a swap occurred, indicating that the list is not yet fully sorted
                                                                                                                                                                                                                my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]

                                                                                                                                                                                                                print(my_list)
