from django.test import TestCase,Client,SimpleTestCase
from django.urls import reverse,resolve
from budget.models import Project,Category,Expense
import json



class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.list_url=reverse('list')
        self.detail_url=reverse('detail',args=['can-be-any-thing-i-want'])
        self.tested_slug=Project.objects.create(name='can-be-any-thing-i-want',budget=1025)
    #test 4
    def test_project_list_GET(self):       
        response=self.client.get(self.list_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response,'budget/project-list.html')
    #test 5
    def test_project_detail_GET(self):       
        response=self.client.get(self.detail_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response,'budget/project-detail.html')
    #test 6 
    def test_project_detail_POST_add(self):
        Category.objects.create(
            project=self.tested_slug,
            name='dev'
        )
        response=self.client.post(self.detail_url,{
            'title':'cap'
        ,'amount':1000,
        'category':'dev'
        })
        self.assertEquals(response.status_code,302)
       
        self.assertEquals(self.tested_slug.expenses.first().title,'cap')
    #test 7
    def test_project_detail_POST_no_data(self):
        response=self.client.post(self.detail_url)
        self.assertEquals(response.status_code,302)
        self.assertEquals(self.tested_slug.expenses.count(),0)
    # test 8
    def test_project_detail_DELETE(self):
        cat1=Category.objects.create(
            project=self.tested_slug,
            name='dev'
        )
        Expense.objects.create(
            project=self.tested_slug,
            title='ex1' ,
            amount=101,
            category=cat1
        )
        response=self.client.delete(self.detail_url,json.dumps({'id':1}))
        self.assertEquals(response.status_code,204)
        self.assertEquals(self.tested_slug.expenses.count(),0)