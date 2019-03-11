from django.db import models


class Newscategory(models.Model):
    name = models.CharField(max_length=120, null=True)
    title = models.CharField(max_length=150, null= True)

    def __str__(self):
        return self.title



class News(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    created_date = models.DateTimeField(auto_now=True)
    written_by = models.CharField(max_length=100)
    image = models.ImageField(upload_to="news")
    category = models.ForeignKey(
        Newscategory, on_delete=models.CASCADE, related_name='news')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-id']
