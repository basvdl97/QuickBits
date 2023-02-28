
if __name__ == "__main__":
    # constant list list
    LIST_SIZE = 20

    # create a list
    alist = [i for i in range(LIST_SIZE)]

    # print the entire list
    print(alist)
    print("")

    # print all the event numbers in the list
    print("even: ", end="")
    for i in range(len(alist)):
        if alist[i] % 2 == 0:
            print(alist[i], end=" ")
    print("\n")

    # print all the odd numbers in the list
    print("odd: ", end="")
    for i in range(len(alist)):
        if alist[i] % 2 == 1:
            print(alist[i], end=" ")
    print("\n")