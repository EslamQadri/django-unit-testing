from unicodedata import category
from django.test import TestCase
from budget.models import Project ,Category,Expense

class TestModels(TestCase):
    def setUp(self):
        self.project1=Project.objects.create(
            name='project 1',
            budget =10000
            )
     #test 9        
    def test_slug_is_create_or_not(self):
        self.assertEquals(self.project1.slug, 'project-1')
    #test 10 
    def test_budget_left(self):
        category1=Category.objects.create(
            project=self.project1,
            name='dev'
        )
        Expense.objects.create(
            project=self.project1,
            title='exp',
            amount=1000,
            category=category1
        )
        Expense.objects.create(
            project=self.project1,
            title='exp1',
            amount=2000,
            category=category1
        )
        self.assertEquals(self.project1.budget_left,7000)
    # test 11
    def test_total_transactions(self):
        project2=Project.objects.create(
            name = 'project2',
            budget =10000

        )
        category1=Category.objects.create(
            project=project2,
            name='dev'
        )
        Expense.objects.create(
            project=project2,
            title='exp',
            amount=1000,
            category=category1
        )
        Expense.objects.create(
            project=project2,
            title='exp1',
            amount=2000,
            category=category1
        )
        self.assertEqual(project2.total_transactions,2)