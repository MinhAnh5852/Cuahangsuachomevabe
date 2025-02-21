from django.db import models

class Revenue(models.Model):
    date = models.DateField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True, null=True)

    class Meta:
        app_label = 'revenue'

    def __str__(self):
        return f"Revenue on {self.date}: {self.amount}"
