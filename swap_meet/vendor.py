
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

    def swap_items(self, other_vendor, my_item, their_item):
        my_item_exists = my_item in self.inventory
        their_item_exists = their_item in other_vendor.inventory
        if not my_item_exists or not their_item_exists:
            return False

        other_vendor.add(self.remove(my_item))
        # self.remove(my_item)
        # other_vendor.add(my_item)

        self.add(other_vendor.remove(their_item))
        # other_vendor.remove(their_item)
        # self.add(their_item)

        return True

    def swap_first_item(self, other_vendor):
        if not self.inventory or not other_vendor.inventory:
            return False
        
        other_vendor.add(self.remove(self.inventory[0]))
        # other_vendor.add(self.inventory[0])
        # self.remove(self.inventory[0])

        self.add(other_vendor.remove(other_vendor.inventory[0]))
        # self.add(other_vendor.inventory[0])
        # other_vendor.remove(other_vendor.inventory[0])

        return True
    
    def get_by_category(self, category):
        list_category = []
        for item in self.inventory:
            if category == item.get_category():
                list_category.append(item)

        return list_category


    def get_best_by_category(self, category):
        list_category = self.get_by_category(category)

        if not list_category:
            return None

        highest_number = 0
  
        for item in list_category:
            if item.condition > highest_number:
                highest_number = item.condition
                highest_item = item
                
        return highest_item
    
    def swap_best_by_category(self, other_vendor, my_priority, their_priority):
        # my_item_list = self.get_by_category(their_priority)
        # their_item_list = other_vendor.get_by_category(my_priority)

        # if not my_item_list or their_item_list:
        #     return False
    
        my_item = self.get_best_by_category(their_priority)
        their_item = other_vendor.get_best_by_category(my_priority)

        if not my_item or not their_item:
            return False
        
        self.swap_items(self, my_item, their_item)

        return True


        
