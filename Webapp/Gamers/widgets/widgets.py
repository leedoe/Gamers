from django import forms
from django.template.loader import render_to_string


class TagsInputWidget(forms.SelectMultiple):
    def render(self, name, value, attrs):
        context = {
            'select_options': [item for item in self.choices],
            'name': name,
        }

        html = render_to_string('widgets/tagsinput.html', context)

        return html


class DatePickerWidget(forms.DateInput):
    def render(self, name, value, attrs):
        context = {
            'name': name,
        }

        html = render_to_string('widgets/datepicker.html', context)

        return html


class StarRatingWidget(forms.NumberInput):
    def render(self, name, value, attrs):
        context = {
            'name': name,
            'value': value,
        }
        html = render_to_string('widgets/starrating.html', context)

        return html
