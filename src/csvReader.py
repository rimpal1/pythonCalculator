import csv
from Calculator import Calculator


# static method
def class_factory(class_name, dictionary):
    return type(class_name, (object,), dictionary)


# makes CsvReader class which will read csv files and put them into a dictionary
class CsvReader:
    data = []

    # constructor
    def __init__(self, filepath):

        # copies csv file to text_data
        with open(filepath) as text_data:
            csv_data = csv.DictReader(text_data, delimiter=',')
            for row in csv_data:
                self.data.append(row)
        pass

    def return_data_as_objects(self, class_name):
        objects = []
        for row in self.data:
            objects.append(class_factory(class_name, row))
        return objects
