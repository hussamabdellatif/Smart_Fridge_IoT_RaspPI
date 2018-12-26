
class Item(object):
        def __init__(self, jsoninput):
                self.id = str(jsoninput['id'])
                self.name = str(jsoninput['name'])
                self.date = str(jsoninput['date'])
                self.quantity = str(jsoninput['quantity'])
