import random
import csv

class City_Information:
    cities_information = []
    
    def __init__(self):
        with open("uscities.csv","r") as cities_file:
            reader = csv.reader(cities_file, quotechar='"')
            next(reader)
            for row in reader:
                necessary_information = [row[0], row[3], row[5], int(row[8]), float(row[9])]
                City_Information.cities_information.append(necessary_information)
                
    def choose_random_city(self):
        random_city_index = random.randint(0,len(City_Information.cities_information))
        random_city = City_Information.cities_information[random_city_index]
        return random_city
            
if __name__ == "__main__":
    city_bank = City_Information()
    myCity = city_bank.choose_random_city()
    print(myCity)