



























def rsum(numbers):
    if not numbers:
        return 0
    else:
        return numbers[0] + rsum(numbers[1:])
    




 







class Node:
    value:int = None

    left:'Node' = None
    right:'Node' = None

    def __init__(self, number:int):
        self.value = number

    def add(self, number:int):
        if number < self.value:
            if self.left:
                self.left.add(number)
            else:
                self.left = Node(number)
        else:
            if self.right:
                self.right.add(number)
            else:
                self.right = Node(number)









class BinaryTree:
    root:'Node' = None

    def add(self, number:int):
        if self.root:
            self.root.add(number)
        else:
            self.root = Node(number)











tree = BinaryTree()
tree.add(1)
tree.add(2)
tree.add(-1)
 














