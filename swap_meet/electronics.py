class Electronics:
    def __init__(self, id, type="Unknown"):
        self.id = id
        self.type = type

    def get_category(self):
        return "Electronics"
    
    def __str__(self):
        return f"An object of type Item with id {self.id}."
