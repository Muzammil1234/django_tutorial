from django.db import models

# Create your models here.
class TodoList(models.Model):
	id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=300)

	def __str__(self):
		return self.name

class Item(models.Model):
	id = models.AutoField(primary_key=True)
	todolist = models.ForeignKey(TodoList, on_delete=models.CASCADE)
	text = models.CharField(max_length=300)
	complete = models.BooleanField()

	def __str__(self):
		return self.text