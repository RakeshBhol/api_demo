from django.db import models
from timezone_field import TimeZoneField

class Member(models.Model):
   id = models.CharField(max_length=9, primary_key=True)
   real_name = models.CharField(max_length=30)
   tz = TimeZoneField(default='Asia/Kolkata')

   def __str__(self):
       return self.id

class Period(models.Model):
   member = models.ForeignKey(Member, on_delete=models.CASCADE, related_name='member')
   start_time = models.DateTimeField()
   end_time = models.DateTimeField()

   def __str__(self):
       return self.start_time
