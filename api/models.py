from django.db import models
from django.utils import timezone

# Create your models here.
# creando la estructura de las tablas
# definiciòn de classe abstracta  para cuando hay campos en comun en varias tablas es una buena practica utilizarla
class AbstractModel(models.Model):
    create_at = models.DateTimeField(default=timezone.now)
    class Meta:
        abstract = True
class Task(AbstractModel):
    title = models.CharField(max_length=180)
    description = models.TextField(null=True, blank=True)
    priority = models.IntegerField(choices=((0,'low'),(1,'medium'),(2,'high')))


    expired_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.id}:  {self.title}"


class Comment(AbstractModel):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='comment_task')
    comment = models.TextField()

