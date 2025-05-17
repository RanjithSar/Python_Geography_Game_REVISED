from city_bank import City_Information
import random

class Question:
    
    city_info = City_Information()
    
    def __init__(self):
        self.question_type = 0
        
    def change_question_type(self, new_type):
        self.question_type = new_type
        
    def generate_question(self):
        
        if self.question_type == 0:
            
            cities = []
            while (len(cities) < 4):
                random_city = Question.city_info.choose_random_city()
                if len(cities) == 0 or random_city[1] not in cities:
                    cities.append(random_city)
                    
            correct_option_index = random.randint(0,3)
            city = cities[correct_option_index]
            
            question = f"What state is {city[0]} from?"
            answers = []
            for i in range(4):
                answers.append(cities[i][1])
            return (question, answers, correct_option_index)
            
        elif self.question_type == 1:
            
            cities = []
            while (len(cities) < 4):
                random_city = Question.city_info.choose_random_city()
                if len(cities) == 0 or random_city[0] not in cities:
                    cities.append(random_city)
                    
            correct_option_index = random.randint(0,3)
            city = cities[correct_option_index]
            
            question = f"Which of these cities is from {cities[correct_option_index][1]}?"
            answers = []
            for i in range(4):
                answers.append(cities[i][0])
            return (question, answers, correct_option_index)
        
        
if __name__ == "__main__":
    first_question = Question()
    print(first_question.generate_question())
    first_question.change_question_type(1)
    print(first_question.generate_question())