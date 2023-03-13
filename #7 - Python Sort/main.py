





# List.sort(reverse, key)
#   - reverse: True | False
#   - key: f() list value to sortable


my_list = [
    ["Honda Civic", 8000],
    ["Toyota Yaris", 7000],
    ["Nissan Skyline", 22000],
]

my_list.sort(key=lambda car: car[1])
print(my_list)













