from django.db import models

# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=False)
    city = models.CharField(max_length=255)
    address = models.TextField(blank=False)

    def to_json(self):
        return{
            'id':self.pk,
            'name':self.name,
            'description':self.description,
            'city':self.city,
            'address':self.address
        }
    class Meta:
        verbose_name = 'Company'
        verbose_name_plural = 'Companies'
        ordering = ('-name','-city')


class Vacancy(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=False)
    salary = models.FloatField()
    company = models.ForeignKey(Company, on_delete=models.CASCADE)


    def to_json(self):
        return{
            'id':self.pk,
            'name':self.name,
            'description':self.description,
            'salary':self.salary,
            'company':self.company.to_json()
        }

    class Meta:
        verbose_name = 'Vacancy'
        verbose_name_plural = 'Vacancies'
        ordering = ('-salary','-name')