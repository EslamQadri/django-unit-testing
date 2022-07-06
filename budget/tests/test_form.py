from django.test import TestCase
from budget.forms import ExpenseForm
class TestForms(TestCase):
    #test 12
    def test_ExpenseForm_valed_date(self):
        form=ExpenseForm(data={
            'title':'any thing',
            'amount':1000,
            'category':'any category'

        })
        self.assertTrue(form.is_valid())
        #test 13
    def test_ExpenseForm_no_data(self):
        form=ExpenseForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors),3)