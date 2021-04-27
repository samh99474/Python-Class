def main():
    global grid_size
    global row_sign
    global col_sign
    row_sign = "-"
    col_sign = "|"
    
    print("Quiz 4")
    row_num = int(input("Numbers of rows:"))
    col_num = int(input("Numbers of colum:"))
    grid_size = int(input("Grid size:"))
    row_sign = row_sign*grid_size

    for i in range(0, row_num+1):
        print(string_row(col_num))
        if i != row_num:
            for j in range(0, grid_size):
                print(string_row2(col_num))
        
def string_row(col_num):
    for i in range(0, col_num):
        if i == 0:
            row = "+" + row_sign + "+"
        else:
            row = row + row_sign + "+"
    return row

def string_row2(col_num):
    for i in range(0, col_num):
        if i == 0:
            col = col_sign + " "*grid_size + col_sign
        else:
            col = col + " "*grid_size + col_sign
    return col
