from email.policy import default
from unicodedata import name
from django.db import models


class directores(models.Model):
   
    name=models.CharField(max_length=64,default="nombre del director")
    last_name=models.CharField(max_length=64,default="apellido del director")
    titulo=models.CharField(max_length=50,help_text="escriba el titulo de la pelicula aqui")
    descripcion=models.TextField(max_length=100,help_text="escribe la descripcion de la pelicula aqui")
    def __str__(self):
        cadena= self.name + "  " +self.last_name+", " +"pelicula:"+self.titulo+"  "+"," +"desripcion:"+" "+self.descripcion
    
        return cadena


        


