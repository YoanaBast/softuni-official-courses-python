class Catalogue:

    def __init__(self, name: str):
        self.name = name
        self.products = []

    def add_product(self, product_name: str):
        self.product_name = product_name
        self.products.append(self.product_name)

    def get_by_letter(self, first_letter: str):
        self.first_letter = first_letter
        self.filtered_list = [pr for pr in self.products if pr[0] == self.first_letter]
        return self.filtered_list

    def __repr__(self):

        return f"Items in the {self.name} catalogue:" + "\n" +\
               '\n'.join(sorted(self.products))

catalogue = Catalogue("Furniture")

catalogue.add_product("Sofa")

catalogue.add_product("Mirror")

catalogue.add_product("Desk")

catalogue.add_product("Chair")

catalogue.add_product("Carpet")

print(catalogue.get_by_letter("C"))

print(catalogue)