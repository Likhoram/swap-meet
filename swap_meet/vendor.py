class Vendor:
    def __init__ (self, inventory=None):
        self.inventory = inventory or []

    def add(self, item):
        self.inventory.append(item)
        return item

    def remove(self, item):
        if item not in self.inventory:
            return False
        self.inventory.remove(item)
        return item
    
    def get_by_id(self, number):
        for item in self.inventory:
            if item.id == number:
                return item
        else:
            return None 
