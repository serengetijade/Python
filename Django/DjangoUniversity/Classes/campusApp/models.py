from django.db import models
#   Python Version: 3.10.8
#
#   Author:     Jade Abreu
#
#   Purpose:    This project is a small part of a larger project - it is a short excercize to create classes and define a model manager.
#
#   Tested OS:  Windows 11

class UniversityCampus(models.Model):
    campus_id = models.IntegerField(primary_key=True)
    campus_name = models.CharField(max_length=60, default="", blank=True, null=False)
    state = models.CharField(max_length=2, default="", blank=True, null=False)

    # Create a model manager
    object = models.Manager()

    #Display the object output values in the form of a string
    def __str__(self):
        display_campus = '{0.campus_id}: {0.campus_name}, {0.state}'
        return display_campus.format(self)

    #define any meta data, like the (plural name)
    class Meta:
        verbose_name = "University Campus"
        verbose_name_plural = "University Campus"