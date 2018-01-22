# Problem 4: Lists and Mutability (Weight 2). Create a list, named yours, to store my favorite
# schools: ‘Yale’, ‘MIT’, and ‘Berkeley’; and create a list, named mine, to store 3 of your favorite schools
# whatever they are. Use the + operator to create a new list, named ours1, to represent our favorite schools:
# ours1 = mine + yours

    yours = ['Yale', 'MIT', 'Berkeley']
    mine = ['Minnesota', 'Harvard', 'Brown']
    ours1 = yours + mine
    print(ours1)

# Now, create another list, name ours2, to again represent our favorite schools but this time use:

    ours2 = []
    ours2.append(yours)
    ours2.append(mine)
    print(ours2)

# 1. Print ours1 and ours2. Describe how ours1 and ours2 differ from each other.

    print(ours1)
    print(ours2)

# In ours1, the + operation adds each element to the list. The length of the list will increase by however many elements
# were in the argument. In this case, 3.
# In ours2, the append operation adds its argument as a single element to the end of a list.
# Thus, the length of the list itself will increase by one.

# 2. Change the second element of yours to something else and again print ours1 and ours2.

    yours[2] = 'Wisconsin'
    print(ours1)
    print(ours2)

# Explain why changing yours would change ours2 but not ours1.
# It depends on the order of the code. yours[2] creates a copy of yours and changes the second element. The ours1
# code does not get changed because the code came before.
