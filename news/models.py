from django.db import models

class Tag(models.Model):
    name = models.CharField('Nome', max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'

class News(models.Model):

    name = models.CharField('Nome', max_length=255)
    content = models.TextField('Conteudo da publicação')
    publication_date = models.DateTimeField('Data de publicacao')
    edition_date = models.DateTimeField('Data de edicao')
    tags = models.ManyToManyField(Tag, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Noticia'
        verbose_name_plural = 'Noticias'
        ordering=['publication_date']