from models import ToDoModel

class ToDoService:
    def __init__(self):
        self.model = ToDoModel()
        
    def create(self, params):
        self.model.create(params["Title"], params["Description"], params["DueDate"], params["UserId"])
        return 'Success'
    
    def show(self):
        return self.model.read_table()
