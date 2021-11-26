from django.db import models
from django.utils import timezone



class TodoList(models.Model): 
    title = models.CharField(max_length=250) 
    content = models.TextField(blank=True) 
    created = models.DateField(default=timezone.now().strftime("%Y-%m-%d")) # a date
    due_date = models.DateField(default=timezone.now().strftime("%Y-%m-%d")) # a date
   
    
    class Meta:
        ordering = ["-created"] #ordering by the created field
    def __str__(self):
        return self.title #name to be shown when called
