"""
Category of an expense
"""

class CategoryList:

    def __init__(self, category_list=None):
        if category_list is not None:
            self.categories = category_list
        else:
            self.categories = []

    def set_categories(self, category_list):
        self.categories = category_list

    def add_category(self, category):
        self.categories.append(category)
