import uuid

class Item:
    def __init__(self, id=None, condition=0):
        self.id = id or uuid.uuid4().int
        self.condition = condition

    def get_category(self):
        return "Item"

    def __str__(self):
        return f"An object of type Item with id {self.id}."
    
    def condition_description(self):
        return f"the value of condition is {self.condition}."
    