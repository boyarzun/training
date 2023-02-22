"""
Following ISP
Interface Segregation Principle

In this example, we have two separate interfaces, Readable and Writable, each containing
only the methods necessary for reading and writing data from a database. The
DatabaseReader and DatabaseWriter classes implement these interfaces, respectively, and
contain the actual implementation for reading and writing data to the database.

The ReportGenerator class only needs to read data from the database, so it only requires
an instance of the Readable interface as a parameter. By specifying the reader parameter
as Readable, we are adhering to the Interface Segregation Principle, as we are not
forcing the ReportGenerator class to implement methods it does not use.

Overall, this implementation demonstrates how the Interface Segregation Principle can be
used to create more modular, maintainable code, by breaking up large interfaces into
smaller, more focused ones.
"""


from abc import ABC, abstractmethod


class Readable(ABC):
    @abstractmethod
    def read(self):
        pass


class Writable(ABC):
    @abstractmethod
    def write(self):
        pass


class DatabaseReader(Readable):
    def read(self):
        # code to read data from database
        pass


class DatabaseWriter(Writable):
    def write(self):
        # code to write data to database
        pass


class ReportGenerator:
    def __init__(self, reader: Readable):
        self.reader = reader

    def generate_report(self):
        data = self.reader.read()
        # code to generate report using data
        pass
