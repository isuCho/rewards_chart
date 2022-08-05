from django.test import TestCase
from parents.models import Child, Parent, Task


class NewChildTest(TestCase):

    def test_can_create_new_child(self):
        self.client.post('/parents/new', data={'child_name': 'Yaes'})
        self.assertEqual(Child.objects.count(), 1)
        created_child = Child.objects.first()
        self.assertEqual(created_child.name, 'Yaes')

    def test_creating_new_child_redirects_to_correct_page(self):
        response = self.client.post('/parents/new', data={'child_name': 'Yaes'})
        parent = Parent.objects.first()
        self.assertRedirects(response, f'/parents/{parent.id}/')


class ChildListTest(TestCase):

    def test_child_list_page_shows_children(self):
        parent_ = Parent.objects.create()
        Child.objects.create(name="Molly", parent=parent_, points=50)
        response = self.client.get(f'/parents/{parent_.id}/')
        self.assertContains(response, 'Molly')


class ChildTaskTest(TestCase):

    def test_can_add_task_to_child(self):
        parent_ = Parent.objects.create()
        child_ = Child.objects.create(name="Molly", parent=parent_)
        Task.objects.create(text="Wash dishes", points=50, child=child_)
        new_task = Task.objects.first()
        self.assertEqual(new_task.text, "Wash dishes")
        self.assertEqual(new_task.points, 50)


class HomePageTest(TestCase):

    def test_home_page_returns_correct_html(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')
        self.assertEqual(response.status_code, 200)

# class NewParentTest(TestCase):
#
#     def test_can_save_a_new_child(self):
#         self.client.post('/parents/new', data={'child_name': 'Able'})
#         self.assertEqual(Child.objects.count(), 1)
#         new_child = Child.objects.first()
#         self.assertEqual(new_child.name, 'Able')
#
#     def test_redirects_after_creating_new_child(self):
#         response = self.client.post('/parents/new', data={'child_name': 'Able'})
#         new_parent = Parent.objects.first()
#         self.assertRedirects(response, f'/parents/{new_parent.id}/')
#
#
# class ChildrenViewTest(TestCase):
#
#     def test_displays_only_children_for_that_parent(self):
#         correct_parent = Parent.objects.create()
#         Child.objects.create(name='Child 1', parent=correct_parent)
#         Child.objects.create(name='Child 2', parent=correct_parent)
#         other_parent = Parent.objects.create()
#         Child.objects.create(name='other child 1', parent=other_parent)
#         Child.objects.create(name='other child 2', parent=other_parent)
#
#         response = self.client.get(f'/parents/{correct_parent.id}/')
#
#         self.assertContains(response, 'Child 1')
#         self.assertContains(response, 'Child 2')
#         self.assertNotContains(response, 'Child 1')
#         self.assertNotContains(response, 'Child 2')
#
#     def test_passes_correct_parent_to_template(self):
#         other_parent = Parent.objects.create()
#         correct_parent = Parent.objects.create()
#         response = self.client.get(f'/parents/{correct_parent.id}/')
#         self.assertEqual(response.context['child_list'], correct_parent)
#
#
# class ChildrenAndParentModelTest(TestCase):
#
#     def test_shows_children(self):
#         parent_ = Parent()
#         parent_.save()
#
#         first_child = Child()
#         first_child.name = 'Gabe'
#         first_child.parent = parent_
#         first_child.save()
#
#         second_child = Child(name='Second')
#         second_child.parent = parent_
#         second_child.save()
#
#         saved_parent = Parent.objects.first()
#         self.assertEqual(saved_parent, parent_)
#
#         saved_items = Child.objects.all()
#         self.assertEqual(saved_items.count(), 2)
#         print(saved_items)
#
#         first_saved_child = saved_items[0]
#         second_saved_child = saved_items[1]
#         self.assertEqual(first_saved_child.name, 'Gabe')
#         self.assertEqual(second_saved_child.name, 'Second')
#         self.assertEqual(first_saved_child.parent, parent_)
#         self.assertEqual(second_saved_child.parent, parent_)
#
#


# #
# #     def test_can_save_child_to_existing_parent(self):
# #         other_parent = Parent.objects.create()
# #         correct_parent = Parent.objects.create()
# #
# #         self.client.post(f'/parents/{correct_parent.id}/add_child', data={'child_name': 'Tasman'})
# #         new_child = Child.objects.first()
# #         self.assertEqual(new_child.name, 'Tasman')
# #         self.assertEqual(new_child.parent, correct_parent)
# #
# #     def test_redirects_to_children_view(self):
# #         other_parent = Parent.objects.create()
# #         correct_parent = Parent.objects.create()
# #
# #         response = self.client.post(f'/parents/{correct_parent.id}/add_child',
# #                                     data={'new_child': 'Child number two'})
# #
# #         self.assertRedirects(response, f'/parents/{correct_parent.id}')
#
