'''
Write a function named printTable() that takes a list of lists of strings and displays it in a well-organized table with each column right-justified. Assume that all the inner lists will contain the same number of strings.

tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

Output: 

   apples Alice  dogs
  oranges   Bob  cats
 cherries Carol moose
   banana David goose

'''

def print_table():
  table_data = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]
  
  # Step 1: Determine column widths
  colWidths = [0] * len(table_data)

  for i in range(len(table_data)):
    colWidths[i] = max(len(item) for item in table_data[i])

  # Step 2: Print the table row-wise
  num_rows = len(table_data[0]) # Assumes all sublists are the same length, 4x4 matrix, etc
  num_cols = len(table_data)

  for row in range(num_rows):
    for col in range(num_cols):
      print(table_data[col][row].rjust(colWidths[col]), end=' ')
    print()

print_table()