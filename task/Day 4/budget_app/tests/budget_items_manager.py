from budget_excel_generator import BudgetExcelGenerator

class BudgetItems(BudgetExcelGenerator):

    def __init__(self):
        super


        self.budget_items = {}

    def add_budget_item(self, item, value):
        self.budget_items[item] = value

    def return_budget_item_value(self, key):
        try:
            return self.budget_items[key]
        except KeyError:
            print("The Key was not found")
            raise

    def delete_budget_item(self, item):
        try:
            del self.budget_items[item]
        except KeyError:
            print("The Key was niot found")
            raise


    def print_budget_item(self):
        print(self.budget_items)

    def save_budget_items(self, file_name_and_path='default'):
        self._create_budget_list(self.budget_items_dict)
        self._save_file_as(file_name_and_path)

# budget = BudgetItems()
# budget._add_budget_item("lunch", 10)
# budget._print_budget_item()
# budget._return_budget_item_value("lunch")

