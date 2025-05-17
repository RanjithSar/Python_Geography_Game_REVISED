cities_file = open("uscities.csv","r")

class City_Information:
    cities_information = []
    def __init__(self):
        for line in cities_file:
            line_list = line.split(",")
            necessary_information = []
            necessary_information.append([line_list[0], line_list[3], line_list[5], line_list[8], line_list[9]])
            City_Information.cities_information.append(necessary_information)
            
if __name__ == "__main__":
    city_bank = City_Information()
    print(city_bank)