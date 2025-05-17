from city_bank import City_Information
import random

class Question:
    
    city_info = City_Information()
    
    def __init__(self):
        self.question_type = 0
        
    def change_question_type(self, new_type):
        self.question_type = new_type
        
    def generate_question(self):
        
        cities = []
        for i in range(4):
            cities.append(Question.city_info.choose_random_city())
            
        print(cities)
        print()
            
        correct_option_index = random.randint(0,3)
        print(cities[correct_option_index])
        
        
if __name__ == "__main__":
    first_question = Question()
    first_question.generate_question()