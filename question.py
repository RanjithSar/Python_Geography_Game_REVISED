from city_bank import City_Information

class Question:
    
    city_info = City_Information()
    
    def __init__(self):
        self.question_type = 0
        
    def change_question_type(self, new_type):
        self.question_type = new_type
        
    def generate_question(self):