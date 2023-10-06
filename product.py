import category from Category

class Product(category.Category):
    def __init__(self, name, description, date_fabrication, is_active):
        self.name = name
        self.description = description
        self.date_fabrication = date_fabrication
        self.is_active = is_active
        
