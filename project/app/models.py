from django.db import models
from autoslug import AutoSlugField

countries = (('ind','india'),
              ('CA', 'Canada'),
              ('MX', 'Mexico'),
              ("1", "One"), 
              ("2", "Two"), 
              ("3", "Three"), 
              ("4", "Four"), 
              ("5", "Five"),
            )

class Student(models.Model):
    Name = models.CharField(max_length=50,verbose_name='Student_name')
    Email = models.EmailField(verbose_name='Student_email')
    Contact = models.IntegerField(verbose_name='Student_contact')
    Add = models.CharField(max_length=100,verbose_name='Student_address')
    Country = models.CharField(max_length=100, choices=countries,null=True)
    New_Slug = AutoSlugField(populate_from='Name',unique = True, null=True,default=None)

    class Meta:
      # If a model is defined outside of applications in INSTALLED_APPS, it must declare which app  it belongs to:
      # app_label = 'app' # add app name here 

      # verbose_name is basically a human-readable name for your model
      # ordering = ["-Name"]
      ordering = ["Name"]  # 
      verbose_name = "stu" # By default, Django will use verbose_name + “s”and reflect on admin pannel.
      # verbose_name_plural = 'Student'
      # The name of the database table to use for the model
      # db_table = 'stu_table'
      # It returns the latest object in the table based on the given field, used for typically DateField, DateTimeField, or IntegerField.
      # get_latest_by = "Name"
      # db_table_comment = "Question answers" 
      