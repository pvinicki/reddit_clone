from django.db import models

class Entry(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    text = models.TextField(max_length=500, blank = True)
    votes = models.IntegerField(default = 0)

    def snippet(self):
        return self.text[:50] + "..."

class Comment(models.Model):
    #parentID = models.IntegerField(default = 0)
    entry = models.ForeignKey(Entry, on_delete=models.CASCADE)
    name = models.CharField(max_length = 50)
    text = models.TextField(max_length = 500, blank = True)
    votes = models.IntegerField(default = 0)
    pub_date = models.DateTimeField('date published')