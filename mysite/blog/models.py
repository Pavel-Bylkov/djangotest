from django.db import models

class Blog(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    tagline = models.TextField(verbose_name='Заголовок')

    def __str__(self):
        return '{}'.format(self.name)

    class Meta:
        verbose_name = "Блог"
        verbose_name_plural = "Блоги"
        ordering = ['-name']

class Author(models.Model):
    name = models.CharField(max_length=200, verbose_name='Имя автора')
    email = models.EmailField()

    def __str__(self):
        return '{}'.format(self.name)

class Entry(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, verbose_name='Название блога')
    headline = models.CharField(max_length=255, verbose_name='Заголовок')
    body_text = models.TextField()
    pub_date = models.DateField(verbose_name='Дата публикации')
    mod_date = models.DateField()
    authors = models.ManyToManyField(Author)
    number_of_comments = models.IntegerField()
    number_of_pingbacks = models.IntegerField()
    rating = models.IntegerField(verbose_name='Рейтинг')

    def __str__(self):
        return '{}'.format(self.headline)
