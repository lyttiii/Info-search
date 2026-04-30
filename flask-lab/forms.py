from flask_wtf import FlaskForm
from wtforms import StringField, DateField, IntegerField, SelectField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length, NumberRange, ValidationError
from datetime import date

class LoginForm(FlaskForm):
    username = StringField('Имя пользователя', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    submit = SubmitField('Войти')


class RegisterForm(FlaskForm):
    username = StringField('Имя пользователя', validators=[DataRequired(), Length(min=3, max=100)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Пароль', validators=[DataRequired(), Length(min=6)])
    name = StringField('Имя', validators=[DataRequired()])
    submit = SubmitField('Зарегистрироваться')


class UniversityForm(FlaskForm):
    full_name = StringField('Полное название', validators=[DataRequired(), Length(max=200)])
    short_name = StringField('Сокращенное название', validators=[DataRequired(), Length(max=50)])
    creation_date = DateField('Дата создания', validators=[DataRequired()])
    submit = SubmitField('Сохранить')
    
    def validate_creation_date(self, field):
        if field.data > date.today():
            raise ValidationError('Дата создания университета не может быть в будущем, введите корректную дату')
        if field.data.year < 1800:
            raise ValidationError('Дата создания не может быть раньше 1800 года, введите корректную дату')


class StudentForm(FlaskForm):
    full_name = StringField('ФИО', validators=[DataRequired(), Length(max=200)])
    birth_date = DateField('Дата рождения', validators=[DataRequired()])
    university_id = SelectField('Университет', coerce=int, validators=[DataRequired()])
    enrollment_year = IntegerField('Год поступления', validators=[DataRequired(), NumberRange(min=1900)])
    submit = SubmitField('Сохранить')
    
    def __init__(self, *args, **kwargs):
        super(StudentForm, self).__init__(*args, **kwargs)
        from models import University
        self.university_id.choices = [(u.id, u.short_name) for u in University.query.all()]
    
    def validate_full_name(self, field):
        words = field.data.strip().split()
        if len(words) != 3:
            raise ValidationError('Введите ФИО полностью')
    
    def validate_birth_date(self, field):
        if field.data > date.today():
            raise ValidationError('Дата рождения не может быть в будущем, введите корректную дату рождения')
        if field.data.year < 1900:
            raise ValidationError('Слишком ранняя дата, укажите дату позднее 1900 г.')
    
    def validate_enrollment_year(self, field):
        current_year = date.today().year
        if field.data > current_year:
            raise ValidationError(f'Год поступления не может быть больше {current_year}')
        if field.data < 1900:
            raise ValidationError('Год поступления не может быть меньше 1900')
    
    def validate(self, extra_validators=None):
        if not super().validate(extra_validators=extra_validators):
            return False
        if self.birth_date.data and self.enrollment_year.data:
            min_year = self.birth_date.data.year + 15
            if self.enrollment_year.data < min_year:
                self.enrollment_year.errors.append(
                    f'Год поступления не может быть раньше {min_year} (минимум 15 лет на момент поступления)'
                )
                return False
        return True

