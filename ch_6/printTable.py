# This program has a function called printzTasble(). It takes a list
# of lists of strings and displays it all as a table with the text
# right justified.

# There has to be a more efficient way to do this. 
def printTable(items):
    colWidths = []
    for i in range(len(items)):
        colWidths.append(len(max(items[i], key=len)))

    just = max(colWidths) + 1

    for i in range(len(items[0])):
        for j in range(len(items)):
            print(items[j][i].rjust(just), end = '')
        print("")   
    



tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

printTable(tableData)

print("")
print("---------")
print("")

tableData = [['John', 'Paul', 'George', 'Ringo'],
             ['Pete', 'Roger', 'John', 'Keith'],
             ['Gordon', 'Brian', 'Blaise', 'John'],
             ['Naoko', 'Ritsuko', 'Atsuko', 'Risa'],
             ['Michael', 'Peter', 'Mike', 'Bill']]

printTable(tableData)

print("")
print("---------")
print("")

# This one has more than 80 cols but works if you make the 
# terminal window wider.
tableData = [['Osaka', 'Kobe', 'Sapporo'],
             ['Boston', 'Washington', 'Winnemucca'],
             ['London', 'Leicestershire', 'Bristol'],
             ['Paris', 'Nice', 'Le Havre'],
             ['Ottawa', 'Kitchener', 'Vancouver'],
             ['Dusseldorf', 'Frankfurt', 'Berlin'],
             ['Glasgow', 'Edinburgh', 'Inverness'],
             ['Melbourne', 'Lightning Ridge', 'Alice Springs']]

printTable(tableData)