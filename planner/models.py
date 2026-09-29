from django.db import models

# Create your models here.
class Module(models.Model):
    name = models.CharField(max_length=200)
    raw_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Topic(models.Model):
    module = models.ForeignKey(
        Module,
        on_delete=models.CASCADE,
        related_name='topics'
    )
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    has_practical = models.BooleanField(default=False)
    priority = models.CharField(max_length=20, default='medium')
    confidence = models.IntegerField(default=1)

    def __str__(self):
        return self.title


class Task(models.Model):
    topic = models.ForeignKey(
        Topic,
        on_delete=models.CASCADE,
        related_name='tasks'
    )
    title = models.CharField(max_length=200)
    task_type = models.CharField(max_length=20)
    estimated_minutes = models.IntegerField(default=30)
    scheduled_date = models.DateField(null=True, blank=True)
    order = models.IntegerField(default=1)
    status = models.CharField(max_length=20, default='not_started')

    def __str__(self):
        return self.title

class Step(models.Model):
    task = models.ForeignKey(
        Task,
        on_delete=models.CASCADE,
        related_name='steps'
    )
    description = models.TextField()
    estimated_minutes = models.IntegerField(default=10)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.description

class Progress(models.Model):
    task = models.OneToOneField(
        Task,
        on_delete=models.CASCADE,
        related_name='progress'
    )
    actual_minutes = models.IntegerField(default=0)
    confidence_before = models.IntegerField(default=1)
    confidence_after = models.IntegerField(default=1)
    notes = models.TextField(blank=True)
    completed_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"Progress for {self.task.title}"


class Plan(models.Model):
    module = models.ForeignKey(
    Module,
    on_delete=models.CASCADE,
    related_name='plans',
    null=True,
    blank=True
    )
    start_date = models.DateField()
    deadline = models.DateField()
    available_hours_per_day = models.FloatField()
    status = models.CharField(max_length=20, default='active')

    def __str__(self):
        return f"Plan: {self.start_date} to {self.deadline}"