#Example of python module. Contains a class called birds
class birds:
    def __init__(self):
        #Create some member animal
        self.members = ['Sparrow', 'Robin', 'Duck', 'Pigeon', 'nightingale']
    
    def printMembers(self):
        print('printing members of the Birds class')
        for member in self.members:
            print('\t%s ' % member)