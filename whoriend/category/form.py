from django import forms
from django.db.models.fields import GenericIPAddressField
from . import models
from users.models import User

class DetailCategoryForm(forms.Form):
    