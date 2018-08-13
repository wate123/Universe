from django.db import models


class Planet(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    radius = models.DecimalField(decimal_places=5, max_digits=15, null=True, blank=True)
    distance = models.DecimalField(decimal_places=15, max_digits=25, null=True, blank=True)
    # temp = models.DecimalField(null=True, blank=True)
    x = models.DecimalField(decimal_places=15, max_digits=25, null=True, blank=True)
    y = models.DecimalField(decimal_places=15, max_digits=25, null=True, blank=True)
    z = models.DecimalField(decimal_places=15, max_digits=25, null=True, blank=True)
    texture_map = models.CharField(max_length=50,null=True, blank=True)
    bump_map = models.CharField(max_length=50,null=True, blank=True)
    specular_map = models.CharField(max_length=50,null=True, blank=True)


class Star(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    radius = models.DecimalField(decimal_places=5, max_digits=15, null=True, blank=True)
    distance = models.DecimalField(decimal_places=15, max_digits=25, null=True, blank=True)
    # temp = models.DecimalField(null=True, blank=True)
    x = models.DecimalField(decimal_places=15, max_digits=25, null=True, blank=True)
    y = models.DecimalField(decimal_places=15, max_digits=25, null=True, blank=True)
    z = models.DecimalField(decimal_places=15, max_digits=25, null=True, blank=True)
    texture_map = models.CharField(max_length=50,null=True, blank=True)
    abs_mag = models.DecimalField(decimal_places=15, max_digits=25, null=True, blank=True)
    color_index = models.DecimalField(decimal_places=15, max_digits=25, null=True, blank=True)
    luminosity = models.DecimalField(decimal_places=10, max_digits=25, null=True, blank=True)