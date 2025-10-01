# import uuid
from .item import Item

class Electronics(Item):
    def __init__(self, id=None, type="Unknown", condition=0):
        # self.id = id or uuid.uuid4().int
        super().__init__(id, condition)
        self.type = type
        # self.condition = condition

    def get_category(self):
        return "Electronics"

    def __str__(self):
        return f"An object of type Electronics with id {self.id}. This is a {self.type} device."

    # def condition_description(self):
    #     return f"the value of condition is {self.condition}."