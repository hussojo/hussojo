from django.db import models

class Book(models.Model):
    name = models.CharField(max_length=300)
    year = models.CharField(max_length=10)

    author = models.CharField(max_length=300, null=True)
    reader_name = models.CharField(max_length=300, null=True)
    comment = models.TextField(max_length=5000, null=True)

    def __str__(self):
        return self.name
        return self.year
        return self.author
        return self.reader_name
        return self.comment

    
