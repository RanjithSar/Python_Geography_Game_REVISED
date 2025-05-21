from city_bank import City_Information
import random

class Question:
    
    city_info = City_Information()
    
    def __init__(self):
        self.question_type = 0
        self.question = ""
        self.answers = []
        self.correct_answer = 0
        
    def change_question_type(self, new_type):
        self.question_type = new_type
        
    def generate_question(self):
        
        if self.question_type == 0:
            
            cities = []
            used_cities = set()
            while (len(cities) < 4):
                random_city = Question.city_info.choose_random_city()
                if random_city[1] not in used_cities:
                    cities.append(random_city)
                    used_cities.add(random_city[1])
                    
            self.correct_answer = random.randint(0,3)
            
            city = cities[self.correct_answer]
            
            self.question = f"What state is {city[0]} from?"
            
            self.answers.clear()
            for i in range(4):
                self.answers.append(cities[i][1])
            
        elif self.question_type == 1:
            
            cities = []
            used_states = set()
            while (len(cities) < 4):
                random_city = Question.city_info.choose_random_city()
                if len(cities) == 0 or random_city[0] not in cities:
                    cities.append(random_city)
                    used_states.add(random_city[0])
                    
            self.correct_answer = random.randint(0,3)
            city = cities[self.correct_answer]
            
            self.question = f"Which of these cities is from {city[1]}?"
            
            self.answers.clear()
            for i in range(4):
                self.answers.append(cities[i][0])
                
        return (self.question, self.answers, self.correct_answer)
        
    def check_correct_answer(self, choice):
        
        if self.answers.index(choice) != self.correct_answer:
            return False
            
        return True
        
        
if __name__ == "__main__":
    first_question = Question()
    question, answers, correct_index = first_question.generate_question()
    for answer in answers:
        print(answer)
    choice = input(question+" ")
    if first_question.check_correct_answer(choice):
        print("Good job!")
    else:
        print(f"Not quite!")
        
    first_question.change_question_type(1)
    question, answers, correct_index = first_question.generate_question()
    for answer in answers:
        print(answer)
    choice = input(question+" ")
    if first_question.check_correct_answer(choice):
        print("Good job!")
    else:
        print(f"Not quite!")