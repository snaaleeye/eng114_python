from NewTestFolder.budget_app.tests.budget_items_manager import BudgetItems
import pytest


class TestBudgetItemsManager:

    budget_item_manager = BudgetItems()

    def test_items_empty_on_initialisation(self):
        assert bool(self.budget_item_manager.budget_items) is False

    def test_add_item_to_budget_list(self):
        self.budget_item_manager.add_budget_item("lunch", 5.50)
        assert self.budget_item_manager.budget_items["lunch"] == 5.50

    def test_budget_item_value_returned(self):
        assert self.budget_item_manager.return_budget_item_value('lunch') == 5.50

    def test_item_is_removed_from_budget_list(self):
        self.budget_item_manager.delete_budget_item("lunch")
        assert bool(self.budget_item_manager.budget_items) is False

    def test_incorrect_key_raises_key_error_for_returning_an_item(self):
        with pytest.raises(KeyError):
            self.budget_item_manager.delete_budget_item("text")