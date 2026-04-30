from django import forms
from .models import University, Student
from datetime import date

class UniversityForm(forms.ModelForm):
    class Meta:
        model = University
        fields = '__all__'
        labels = {
            'full_name': 'Полное название',
            'short_name': 'Сокращенное название',
            'creation_date': 'Дата создания',
        }
        widgets = {
            'creation_date': forms.DateInput(attrs={'type': 'date'}),
        }

    def clean_creation_date(self):
        value = self.cleaned_data["creation_date"]
        if value > date.today():
            raise forms.ValidationError("Дата создания университета не может быть в будущем.")
        if value.year < 1800:
            raise forms.ValidationError("Дата создания не может быть раньше 1800 года.")
        return value

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
        labels = {
            'full_name': 'ФИО',
            'birth_date': 'Дата рождения',
            'university': 'Университет',
            'enrollment_year': 'Год поступления',
        }
        widgets = {
            'birth_date': forms.DateInput(attrs={'type': 'date'}),
        }

    def clean_full_name(self):
        fio = self.cleaned_data['full_name'].strip()
        if len(fio.split()) != 3:
            raise forms.ValidationError('Введите ФИО полностью: фамилия, имя и отчество (3 слова)')
        return fio

    def clean_birth_date(self):
        birth = self.cleaned_data['birth_date']
        if birth > date.today():
            raise forms.ValidationError('Дата рождения не может быть в будущем')
        if birth.year < 1900:
            raise forms.ValidationError('Дата рождения слишком ранняя, укажите корректную дату после 1900 года')
        return birth

    def clean_enrollment_year(self):
        year = self.cleaned_data['enrollment_year']
        current = date.today().year
        if year > current:
            raise forms.ValidationError(f'Год поступления не может быть больше {current}')
        if year < 1900:
            raise forms.ValidationError('Год поступления не может быть меньше 1900')
        return year

    def clean(self):
        cleaned = super().clean()
        birth = cleaned.get('birth_date')
        enrollment_year = cleaned.get('enrollment_year')
        if birth and enrollment_year:
            if enrollment_year < (birth.year + 15):
                raise forms.ValidationError(f'Год поступления не может быть раньше {birth.year+15} (минимум 15 лет на момент поступления)')
        return cleaned

