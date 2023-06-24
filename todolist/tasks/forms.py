from django import forms
from django.core.exceptions import ValidationError

from .models import Todo, Tag


class TodoForm(forms.ModelForm):
    tag = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

    class Meta:
        model = Todo
        fields = "__all__"


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ['name']

    def clean_license_number(self):
        name = self.cleaned_data["name"]

        if name in Tag.objects.all():
            raise ValidationError(
                "Driver's license number must consist of exactly 8 characters."
            )

        return name
