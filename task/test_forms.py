from django.test import TestCase
from .forms import TaskForm

# Create your tests here.


class TestTaskForm(TestCase):

    def test_task_form_vis_required(self):

        form = TaskForm({'task': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('task', form.errors.keys())

    def test_done_field_is_not_required(self):
        form = TaskForm({'task': 'Test Todo Task'})
        self.assertTrue(form.is_valid())

    def test_fields_are_explicit_in_form_metaclass(self):
        form = TaskForm()
        self.assertEqual(form.Meta.fields, ['task', 'done'])
