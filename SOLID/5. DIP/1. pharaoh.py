"""
Following DIP
Dependency Inversion Principle

In this example, the Pharaoh class represents the high-level module, the Foreman class
represents the abstraction, and the Laborer class represents the low-level module. The
Pharaoh class communicates with the Foreman class, which in turn communicates with the
Laborer class. This demonstrates how the high-level module depends on the abstraction
or interface, rather than on the specific implementation details of the low-level module.
"""


class Pharaoh:
    def __init__(self, foreman):
        self.foreman = foreman

    def instruct(self):
        self.foreman.instruct()


class Foreman:
    def __init__(self, laborer):
        self.laborer = laborer

    def instruct(self):
        self.laborer.work()


class Laborer:
    def work(self):
        print("Moving stones")


laborer = Laborer()
foreman = Foreman(laborer)
pharaoh = Pharaoh(foreman)

pharaoh.instruct()  # Outputs "Moving stones"


"""
NOT Following DIP
Dependency Inversion Principle
"""


class Pharaoh:
    def __init__(self, laborer):
        self.laborer = laborer

    def instruct(self):
        self.laborer.work()


class Laborer:
    def work(self):
        print("Moving stones")


laborer = Laborer()
pharaoh = Pharaoh(laborer)

pharaoh.instruct()  # Outputs "Moving stones"
