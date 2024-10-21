from django.db import models

# Create your models here.


class Faq(models.Model):

    question = models.CharField(max_length=254)
    answer = models.CharField(max_length=254)

    def __str__(self):
        return self.question


class Question(models.Model):
    name = models.CharField(max_length=254)
    email = models.EmailField(max_length=254)
    question_asked = models.CharField(max_length=254)

    def __str__(self):
        return self.question_asked
