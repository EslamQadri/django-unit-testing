from django.test import SimpleTestCase
from django .urls import reverse,resolve
from budget.views import project_list,project_detail,ProjectCreateView

class TestUrl(SimpleTestCase):
    def test_list_urls_is_resolved(self):
        url = reverse('list')
        print(resolve(url))
        #check if go to right function
        self.assertEquals(resolve(url).func,project_list)
    def test_ProjectCreateView_is_resolved(self):
        url = reverse('add')
        print(resolve(url))
        #check if go to right function
        self.assertEquals(resolve(url).func.view_class,ProjectCreateView)#.view_class used in Class based views
    def test_project_detail_is_resolved(self):
        url = reverse('detail',args=['some-thing'])
        print(resolve(url))
        #check if go to right function
        self.assertEquals(resolve(url).func,project_detail)

