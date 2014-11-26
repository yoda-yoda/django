from django.db import models

# Create your models here.
class Article(models.Model):
	#kind of members
	title = models.CharField(max_length=200)
	body = models.TextField()
	pub_date = models.DateTimeField('date published')
	likes = models.IntegerField()

	#language unicode, to display some info in class.objects.all() <Classname: title>
	def __unicode__(self):
		return self.title
	
	
