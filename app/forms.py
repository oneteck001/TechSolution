from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Email, Length, EqualTo


class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Пароль", validators=[DataRequired()])
    remember = BooleanField("Запомнить меня")
    submit = SubmitField("Войти")


class RegisterForm(FlaskForm):
    full_name = StringField("ФИО", validators=[DataRequired(), Length(min=2, max=150)])
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Пароль", validators=[DataRequired(), Length(min=6)])
    confirm = PasswordField("Повторите пароль", validators=[EqualTo("password")])
    submit = SubmitField("Зарегистрироваться")


class NewsForm(FlaskForm):
    title = StringField("Заголовок", validators=[DataRequired(), Length(max=200)])
    body = TextAreaField("Текст", validators=[DataRequired()])
    submit = SubmitField("Сохранить")


class JobForm(FlaskForm):
    title = StringField("Должность", validators=[DataRequired()])
    department = StringField("Отдел")
    location = StringField("Локация")
    employment_type = StringField("Тип занятости")
    description = TextAreaField("Описание", validators=[DataRequired()])
    submit = SubmitField("Сохранить")


class ContactForm(FlaskForm):
    name = StringField("Имя", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired(), Email()])
    subject = StringField("Тема", validators=[DataRequired()])
    message = TextAreaField("Сообщение", validators=[DataRequired()])
    submit = SubmitField("Отправить")


class JobApplicationForm(FlaskForm):
    name = StringField("Имя", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired(), Email()])
    phone = StringField("Телефон")
    message = TextAreaField("Сообщение")
    submit = SubmitField("Отправить")

