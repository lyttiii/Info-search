from flask import render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from app import app, db
from models import University, Student, User
from forms import UniversityForm, StudentForm, LoginForm, RegisterForm

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and check_password_hash(user.password, form.password.data):
            login_user(user)
            return redirect(url_for('index'))
        flash('Неверное имя пользователя или пароль')
    return render_template('login.html', form=form)


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        if User.query.filter_by(username=form.username.data).first():
            flash('Пользователь с таким именем уже существует')
            return render_template('register.html', form=form)
        if User.query.filter_by(email=form.email.data).first():
            flash('Пользователь с таким email уже существует')
            return render_template('register.html', form=form)
        
        user = User(
            username=form.username.data,
            email=form.email.data,
            password=generate_password_hash(form.password.data),
            name=form.name.data
        )
        db.session.add(user)
        db.session.commit()
        flash('Регистрация успешна! Теперь вы можете войти.')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/university/')
def university_list():
    universities = University.query.all()
    return render_template('university_list.html', universities=universities)


@app.route('/university/create', methods=['GET', 'POST'])
@login_required
def create_university():
    form = UniversityForm()
    if form.validate_on_submit():
        university = University(
            full_name=form.full_name.data,
            short_name=form.short_name.data,
            creation_date=form.creation_date.data
        )
        db.session.add(university)
        db.session.commit()
        flash('Университет успешно создан!')
        return redirect(url_for('university_list'))
    return render_template('create_university.html', form=form)


@app.route('/university/edit/<int:university_id>', methods=['GET', 'POST'])
@login_required
def edit_university(university_id):
    university = University.query.get_or_404(university_id)
    form = UniversityForm(obj=university)
    if form.validate_on_submit():
        university.full_name = form.full_name.data
        university.short_name = form.short_name.data
        university.creation_date = form.creation_date.data
        db.session.commit()
        flash('Университет успешно обновлен!')
        return redirect(url_for('university_list'))
    return render_template('edit_university.html', form=form, university=university)


@app.route('/university/delete/<int:university_id>')
@login_required
def delete_university(university_id):
    university = University.query.get_or_404(university_id)
    db.session.delete(university)
    db.session.commit()
    flash('Университет успешно удален!')
    return redirect(url_for('university_list'))


@app.route('/student/')
def student_list():
    students = Student.query.all()
    return render_template('student_list.html', students=students)


@app.route('/student/create', methods=['GET', 'POST'])
@login_required
def create_student():
    form = StudentForm()
    if form.validate_on_submit():
        student = Student(
            full_name=form.full_name.data,
            birth_date=form.birth_date.data,
            university_id=form.university_id.data,
            enrollment_year=form.enrollment_year.data
        )
        db.session.add(student)
        db.session.commit()
        flash('Студент успешно создан!')
        return redirect(url_for('student_list'))
    if not form.university_id.choices:
        flash('Сначала создайте хотя бы один университет')
        return redirect(url_for('university_list'))
    return render_template('create_student.html', form=form)


@app.route('/student/edit/<int:student_id>', methods=['GET', 'POST'])
@login_required
def edit_student(student_id):
    student = Student.query.get_or_404(student_id)
    form = StudentForm(obj=student)
    if form.validate_on_submit():
        student.full_name = form.full_name.data
        student.birth_date = form.birth_date.data
        student.university_id = form.university_id.data
        student.enrollment_year = form.enrollment_year.data
        db.session.commit()
        flash('Студент успешно обновлен!')
        return redirect(url_for('student_list'))
    form.university_id.data = student.university_id
    return render_template('edit_student.html', form=form, student=student)


@app.route('/student/delete/<int:student_id>')
@login_required
def delete_student(student_id):
    student = Student.query.get_or_404(student_id)
    db.session.delete(student)
    db.session.commit()
    flash('Студент успешно удален!')
    return redirect(url_for('student_list'))

