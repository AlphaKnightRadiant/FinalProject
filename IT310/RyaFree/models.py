from django.db import models

# Create your models here.
class Question(models.Model):
    questionText = models.CharField(max_length=264, unique = True)

    def __str__(self):
        return self.questionText

class Option(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    OptionName = models.CharField(max_length=264, unique=True)
    votes = models.IntegerField(default = 0)

    def __str__(self):
        return self.OptionName

class AccessRecord(models.Model):
    name = models.ForeignKey(Option, on_delete=models.CASCADE)
    date = models.DateField()

    def __str__(self):
        return str(self.date)
