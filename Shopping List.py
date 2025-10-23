class ShoppingList:
    def __init__(self):
        self.shopping_list = []

    def add_item(self):
        pass

    def get_num_items(self):
        pass

    def get_list_of_items(self):
        pass

    def remove_item(self):
        pass

class ShoppingItem:
    def __init__(self, item_name, item_quantity):
       self._item_name = item_name
       self._item_quantity = item_quantity

    
    @property
    def item_name(self):
        return self._item_name

    @property
    def item_quantity(self):
        return self._item_quantity
    
    @item_quantity.setter
    def item_quantity(self, item_quantity):
        self._item_quantity = item_quantity

item1 = ShoppingItem("apples", 6)
print(f"{item1.item_name}: {item1.item_quantity}")
item2 = ShoppingItem("kiwis", 7)
print(f"{item2.item_name}: {item2.item_quantity}")