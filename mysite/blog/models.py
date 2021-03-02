from django.db import models

class Blog(models.Model):
    name = models.CharField(max_length=100)
    tagline = models.TextField()
    url = models.URLField()

    def __str__(self):
        return '{}'.format(self.name)

class Author(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()

    def __str__(self):
        return '{}'.format(self.name)

class Entry(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    headline = models.CharField(max_length=255)
    body_text = models.TextField()
    published = models.BooleanField(default=True)
    pub_date = models.DateField()
    mod_date = models.DateField()
    authors = models.ManyToManyField(Author, related_name="posts")
    number_of_comments = models.IntegerField()
    number_of_pingbacks = models.IntegerField()
    rating = models.IntegerField()

    def __str__(self):
        return '{}'.format(self.headline)
