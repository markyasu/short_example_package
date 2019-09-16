# importing classes from the "nations" package


from nations.Europe import Europe
from nations.Asia import Asia

# creating objects of europe and asia classes, then calling them
european_nations = Europe()
european_nations.printMembers()

asian_nations = Asia()
asian_nations.printMembers()

