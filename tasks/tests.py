from django.test import TestCase
from tasks.models import Task
from tasks.utils import calculate_priority
from datetime import date, timedelta

class TaskPriorityTests(TestCase):

    def test_basic_priority(self):
        task = Task.objects.create(
            title="Task1",
            due_date=date.today() + timedelta(days=2),
            estimated_hours=2,
            importance=8
        )
        task.dependencies.set([])
        score = calculate_priority(task)
        self.assertTrue(score > 0)

    def test_past_due_task(self):
        past_date = date.today() - timedelta(days=3)
        task = Task.objects.create(
            title="PastTask",
            due_date=past_date,
            estimated_hours=2,
            importance=5
        )
        task.dependencies.set([])
        score = calculate_priority(task)
        self.assertTrue(score > 0)  # just check score is positive

    def test_with_dependencies(self):
        task1 = Task.objects.create(
            title="Task1",
            due_date=date.today() + timedelta(days=2),
            estimated_hours=2,
            importance=7
        )
        task2 = Task.objects.create(
            title="Task2",
            due_date=date.today() + timedelta(days=3),
            estimated_hours=3,
            importance=6
        )
        task2.dependencies.set([task1])
        score = calculate_priority(task2)
        self.assertTrue(score > 0)