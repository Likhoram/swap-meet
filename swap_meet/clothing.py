class Clothing:
    def __init__(self, id, fabric="Unknown"):
        self.id = id
        self.fabric = fabric

    def get_category(self):
        return "Clothing"
    
    def __str__(self):
        return f"An object of type Item with id {self.id}."