from django.db import models
from django.contrib.auth.models import User


class Backtest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    input_parameters = models.JSONField()
    output_results = models.JSONField()
    timestamp = models.DateTimeField(auto_now_add=True)

class LoginHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

class RegisterHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} - {self.timestamp}'    

