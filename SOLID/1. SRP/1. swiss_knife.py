"""
Following SRP
Single Responsability Principle

In this version, the responsibilities of cutting, trimming, opening cans, and tightening screws
are delegated to separate classes that each have a single responsibility. The SwissArmyKnife
class is responsible only for managing these separate classes and providing a public interface
for their functionality. By breaking down the responsibilities in this way, we can more easily
modify or extend the behavior of each individual component without affecting the others.
"""


class Knife:
    def cut(self, item):
        print(f"Cutting {item} with knife")


class Scissors:
    def trim(self, item):
        print(f"Trimming {item} with scissors")


class CanOpener:
    def open(self, can):
        print(f"Opening {can} with can opener")


class Screwdriver:
    def tighten(self, screw):
        print(f"Tightening {screw} with screwdriver")


class SwissArmyKnife:
    def __init__(self):
        self._knife = Knife()
        self._scissors = Scissors()
        self._can_opener = CanOpener()
        self._screwdriver = Screwdriver()

    def cut(self, item):
        self._knife.cut(item)

    def trim(self, item):
        self._scissors.trim(item)

    def open_can(self, can):
        self._can_opener.open(can)

    def tighten_screw(self, screw):
        self._screwdriver.tighten(screw)


"""
NOT Following SRP
Single Responsability Principle

In this example, the SwissArmyKnife class has multiple responsibilities - cutting, trimming,
opening cans, and tightening screws. This violates the Single Responsibility Principle because
the class should only have one reason to change, but in this case, it has multiple reasons to change.

To fix this violation, we can break down the responsibilities of the SwissArmyKnife class into
smaller, more focused classes that each have a single responsibility. For example, we could
create a Knife class, a Scissors class, a CanOpener class, and a Screwdriver class, each of
which has a single responsibility. This would result in more maintainable and modular code.
"""


class SwissArmyKnife:
    def __init__(self):
        pass

    def cut(self, item):
        print("Cut")

    def trim(self, item):
        print("Trim")

    def open_can(self, can):
        print("Open")

    def tighten_screw(self, screw):
        print("Tighten")
