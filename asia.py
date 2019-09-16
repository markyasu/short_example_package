class Asia:
    def __init__(self):
        # create asian nation members
        self.members = ['Azerbaijan', 'Brunei', 'China']

    def printMembers(self):
        print('Printing members of the Asia class')
        for member in self.members:
            print('\t%s ' % member)