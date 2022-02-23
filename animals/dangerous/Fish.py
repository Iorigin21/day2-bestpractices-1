# Example of python module. Contains a class called fish
class fish:
    def __init__(self):
        # Create some member animal
        self.members = ['Shark', 'Killer Whale', 'Piranha']

    def printMembers(self):
        print('printing members of the Fish class')
        for member in self.members:
            print('\t%s ' % member)