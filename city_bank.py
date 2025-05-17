import random
import csv

class City_Information:
    
    # The class list
    cities_information = []
    
    '''
    It opens the uscities.csv file in the root directory, skipping the first header row,
    and collects the city name, state name, county name, population, and population density
    for each city from each row and stores the information in a list.
    This list for each individual city is then appended to the class list cities_information.
    '''
    with open("uscities.csv","r") as cities_file:
        reader = csv.reader(cities_file, quotechar='"')
        next(reader)
        for row in reader:
            necessary_information = [row[0], row[3], row[5], int(row[8]), float(row[9])]
            cities_information.append(necessary_information)
    
    '''
    Initializes a new city bank. 
    Since the information is already loaded when the class is defined, each new city 
    bank instance can access the full list upon creation.
    '''
    def __init__(self):
        pass
    
    '''
    Returns a random city list from the class list.
    '''
    def choose_random_city(self):
        random_city_index = random.randint(0,len(City_Information.cities_information))
        random_city = City_Information.cities_information[random_city_index]
        return random_city
   
'''
FOR TESTING PURPOSES
'''   
if __name__ == "__main__":
    city_bank = City_Information()
    myCity = city_bank.choose_random_city()
    print(myCity)