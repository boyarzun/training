"""
Following OCP
Open Close Principle

In this example, ToyBlock represents the base class that is closed to modification. RedBlock,
BlueBlock, and GreenBlock are examples of classes that extend ToyBlock to create new types of
blocks. The BlockSet class represents a set of blocks that can be extended by adding new blocks
to the list.

By creating new classes that inherit from ToyBlock, we are able to extend the functionality of
the code without modifying the existing behavior of the ToyBlock class. This is an example of
following the Open-Closed Principle.
"""


class ToyBlock:
    def __init__(self, size, shape, color):
        self.size = size
        self.shape = shape
        self.color = color

    def combine(self, other_block):
        # method to combine blocks
        pass


class RedBlock(ToyBlock):
    def __init__(self, size, shape):
        super().__init__(size, shape, "red")


class BlueBlock(ToyBlock):
    def __init__(self, size, shape):
        super().__init__(size, shape, "blue")


class GreenBlock(ToyBlock):
    def __init__(self, size, shape):
        super().__init__(size, shape, "green")


class BlockSet:
    def __init__(self, blocks):
        self.blocks = blocks

    def add_block(self, new_block):
        self.blocks.append(new_block)

    def build_structure(self):
        # method to build a structure using the blocks
        pass


"""
NOT Following OCP
Open Close Principle

In this example, we have created a new type of block called MultiColoredBlock which has two colors
instead of one. While this new functionality may be useful, it violates the Open-Closed Principle
because it requires modifying the existing ToyBlock class to accommodate the additional color parameter.

If we continue to add new types of blocks by modifying the existing ToyBlock class in this way, it
will become more and more difficult to maintain and modify the code. Therefore, it is better to extend
the behavior of the ToyBlock class by creating new classes that inherit from it, rather than modifying
it directly.
"""


class ToyBlock:
    def __init__(self, size, shape, color):
        self.size = size
        self.shape = shape
        self.color = color

    def combine(self, other_block):
        # method to combine blocks
        pass


class BlockSet:
    def __init__(self, blocks):
        self.blocks = blocks

    def add_block(self, new_block):
        self.blocks.append(new_block)

    def build_structure(self):
        # method to build a structure using the blocks
        pass


class MultiColoredBlock(ToyBlock):
    def __init__(self, size, shape, color1, color2):
        super().__init__(size, shape, color1)
        self.color2 = color2
