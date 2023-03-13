







# create a list
my_list = []

# option 1 - append
my_list.append("Option 1")

# option 2 - +
my_list += ["Option 2"]

# option 3 - deconstruct and repack
my_list = [*my_list, "Option 3"]

# option 4 - extend
my_list.extend(["Option 4"])

print('\n'.join(my_list))