import csv

#http, обработчик ошибок,

# get запрост по адрес
# regex
#urllib3 python, requests python, http, regex

class Input_Output_Manager:
    def __init__(self):
        self.file = ""

    def read(self, file_address):
        with open(file_address, 'r') as file:
            csvreader = csv.reader(file)
            new_ref = []
            for row in csvreader:
                new_ref.append(row)
            new_ref.pop(0)
            return new_ref




