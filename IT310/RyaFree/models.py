from django.db import models
#from multiselectfield import multiselectfield
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

'''
class multiOption(models.Model):
    CHOICES1 = (("A","Are you Free Monday?"),
                ("B","Are You Free Teusday?"),
                ("C","Are You Free Wednesday?"),
                ("D","Are You Free Thursday?"),
                ("E","Are You Free Friday?"),
                ("F","Are You Free Saturday?"),
                ("G","Are You Free Sunday?"),
                                            )
    CHOICES2 = ((1, "Yes"),
                (2, "sorry, no!"),)

    my_field = multiselectfield(choices = CHOICES1)
    my_field2= multiselectfield(choices = CHOICES2,max_choices=3,max_length = 3)
'''
