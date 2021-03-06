from django.db import models

# Create your models here.

class Cursus(models.Model):
  name = models.CharField(
    max_length=50,
    blank=False,
    null=True,
    default='aucun'
  )
  year_from_bac = models.SmallIntegerField(
    help_text = "year since le bac",
    verbose_name="year",
    blank=False,
    null=True,
    default=0
  )
  scholar_year = models.CharField(
    max_length=9,
    blank=False,
    null=True,
    default='0000-00001'
  )

  class Meta:
    constraints = [
      models.UniqueConstraint(fields=['name'], name='unicite nom')
    ]

class Student(models.Model):
  first_name = models.CharField (
    max_length = 50,
    blank=False,
    null=False
  )
  birth_date = models.DateField(
    verbose_name='date of birth',
    blank=False,
    null=False
  )
  last_name = models.CharField(
    verbose_name="lastname",
    help_text="last name of the student",
    blank=False, #pas de champ vide
    null=False, #pas de champ null (a conjuguer avec default)
    default="???",
    max_length=255, #taille maximale du champ
  )
  phone = models.CharField(
    verbose_name="phonenumber",
    help_text="phone number of the student",
    blank=False, #pas de champ vide
    null=False, #pas de champ null (a conjuguer avec default)
    default="0999999999",
    max_length=10, #taille maximale du champ
  )
  email = models.CharField(
    verbose_name="emal",
    help_text="email of the student",
    blank=False, #pas de champ vide
    null=False, #pas de champ null (a conjuguer avec default)
    default="x@y.z",
    max_length=255, #taille maximale du champ
  )
  comments = models.CharField(
    verbose_name="comments",
    help_text="some comments about the student",
    blank=True,
    null=False, #pas de champ null (a conjuguer avec default)
    default="",
    max_length=255, #taille maximale du champ
  )
  cursus = models.ForeignKey(
    Cursus,
    on_delete=models.CASCADE, #necessaire selon la version de Django
    null=True
  )

  class Meta:
    constraints = [
        models.UniqueConstraint(fields=['first_name', 'last_name'], name='unicite prenom nom')
    ]

class Presence(models.Model):
  reason = models.CharField (
    max_length = 50,
    blank=False,
    null=False
  )
  isMissing = models.BooleanField (
    blank=False,
    null=False
  )
  date = models.DateField(
    verbose_name='date',
    blank=False,
    null=False
  )
  student = models.ForeignKey(
    Student,
    on_delete=models.CASCADE, #necessaire selon la version de Django
    null=True
  )