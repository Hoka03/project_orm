from django import forms

from apps.to_do.models import ToDo


class ToDoForm(forms.ModelForm):
    class Meta:
        model = ToDo
        exclude = ('done', 'done_at')