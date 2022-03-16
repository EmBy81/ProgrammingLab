def sum_list(values):
    totale=0
    for item in values:
        totale += item
    return totale
    
def sum_csv(file_name):
    values = []
    my_file = open('shampoo_sales.csv', 'r')
    for line in my_file:
        elements = line.split(',')
        if elements[0] != 'Date':
            date = elements[0]
            value = elements[1]
            values.append(float(value))
    my_file.close()
    return sum_list(values)
     
print(sum_csv('shampoo_sales.csv'))