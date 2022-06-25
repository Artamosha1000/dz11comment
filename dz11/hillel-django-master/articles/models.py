from django.db import models

class Article(models.Model):
	id = models.AutoField(primary_key=True)
	title = models.CharField(max_length=40)
	content = models.TextField()
	creator_name = models.CharField(max_length=100)
	updated_at = models.DateTimeField(auto_now=True)
	created_at = models.DateTimeField(auto_now_add=True)
