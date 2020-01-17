# This program has a function called printzTasble(). It takes a list
# of lists of strings and displays it all as a table with the text
# right justified.

# There has to be a more efficient way to do this. 
def printTable(items):
    colWidths = []
    for i in range(len(items)):
        colWidths.append(len(max(items[i], key=len)))

    just = max(colWidths)

    for i in range(len(items[0])):
        for j in range(len(items)):
            print(items[j][i].rjust(just), end = '')
        print("")   
    



tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

printTable(tableData)