from django.db import models


class Reporter(models.Model):
    full_name = models.CharField(max_length=70)


class Article(models.Model):
    pub_date = models.DateField()
    reporter = models.ForeignKey(Reporter, on_delete=models.CASCADE)
