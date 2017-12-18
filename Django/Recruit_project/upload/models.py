# -*- coding: utf-8 -*-
from django.db import models
import uuid
import os
# Create your models here.

class Document(models.Model):
	docfile = models.FileField(upload_to='uploads/')

class Document1(models.Model):
	docfile = models.FileField(upload_to='uploads1/')

class Document2(models.Model):
	docfile = models.FileField(upload_to='uploads2/')

class Document3(models.Model):
	docfile = models.FileField(upload_to='uploads3/')