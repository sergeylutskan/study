# Create a table of operation from lambda function

def print_operation_table(operation, num_rows=9, num_columns=9):
    for x in range(1,num_rows+1):
        row = []
        for y in range(1,num_columns+1):
            result = list(map(operation,[x],[y]))
            row = row + result
        print(*row,sep='\t')




print_operation_table(lambda x, y: x * y,5,6) 
