from django.db import models

class Auxiliares(models.Model):
    id = models.IntegerField(db_column='Id', blank=True, null=True, help_text='Identificador del Auxiliar.')
    title = models.CharField(db_column='Title', max_length=120, blank=True, null=True, help_text='Nombre del Auxiliar.')
    
    def __str__(self):
        return self.title
    
    class Meta:
        managed = False  
        verbose_name = "Auxiliar"
        verbose_name_plural = "Auxiliares" 
