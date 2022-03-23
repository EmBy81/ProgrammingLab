class CSVfile():
    def __init__(self, name):
        self.name = name
    def __str_(self):
        return 'Name file is {}'.format(self.name)
    def get_data(self):
        values = []
        my_file = open(self.name, 'r')
        for line in my_file:
            elements = line.split(',')
            elements[-1] = elements[-1].strip()
            if elements[0] != 'Date':
                #date = elements[0]
                #value = elements[1]
                #values.append(date)
                #values.append(value)
                #values.append([date,value])                
                values.append(elements)
        my_file.close()
        return values

# csvfile = Csvfile('ciao.txt')
# per far passare, commento anche quei due sotto
# csvfile = CSVfile('shampoo_sales.csv')
# print(csvfile.get_data())

