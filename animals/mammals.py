class mammals:
    def __init__(self):
        # Create some member animal
        self.members = ['Tiger','Elephant','Wild Cat','Dog','Marmot']

    def printMembers(self):
        print('printing members of the mammals class')
        for member in self.members:
            print('\t%s ' % member)