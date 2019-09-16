class Europe:
    def __init__(self):
        # create eurpoean members
        self.members = ['France', 'Germany', 'Estonia']

    def printMembers(self):
        print('Printing members of the Europe class')
        for member in self.members:
            print('\t%s ' % member)