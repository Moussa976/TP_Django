from django.db import models

class Task(models.Model):
    content = models.CharField(max_length=255)
    is_done = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.content + ' | ' + str(self.is_done)