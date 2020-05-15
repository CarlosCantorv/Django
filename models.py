from django.db import models
from datetime import datetime

class Empleado(models.Model):
    Emp_nom = models.CharField(max_length=50, verbose_name='Nombres')
    Emp_ide = models.CharField(max_length=10, verbose_name='Cedula')
    Emp_FeR = models.DateField(default=datetime.now, verbose_name='FechaR')
    Emp_FeC = models.DateTimeField(auto_now=True)
    Emp_FeU = models.DateTimeField(auto_now_add=True)
    Emp_eda = models.PositiveIntegerField(default=0)
    Emp_sal = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    Emp_sta = models.BooleanField(default=True)
    Emp_ava = models.ImageField(upload_to='Avatar%Y%m%d', null=True, blank=True)
    Emp_cvi = models.FileField(upload_to='Cvitae%Y%m%d', null=True, blank=True)

def __str__(self):
    return self.Emp_nom

class Meta:
    verbose_name = 'Empleado'
    verbose_name_plural = 'Empleados'
    db_table = 'empleado'
    ordering = ['id']

