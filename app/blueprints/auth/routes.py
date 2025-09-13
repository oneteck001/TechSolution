from flask import render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, login_required, current_user
from . import auth_bp
from ...forms import LoginForm, RegisterForm
from ...models import User, Role
from ...extensions import db


@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("dashboard.index"))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data.lower()).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember.data)
            next_url = request.args.get("next") or url_for("dashboard.index")
            flash("С возвращением!", "success")
            return redirect(next_url)
        flash("Неверный email или пароль", "danger")
    return render_template("auth/login.html", form=form)


@auth_bp.route("/register", methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for("dashboard.index"))
    form = RegisterForm()
    if form.validate_on_submit():
        if User.query.filter_by(email=form.email.data.lower()).first():
            flash("Такой email уже зарегистрирован", "warning")
            return render_template("auth/register.html", form=form)
        user = User(full_name=form.full_name.data, email=form.email.data.lower())
        user.set_password(form.password.data)
        role = Role.query.filter_by(name="user").first()
        if role:
            user.roles.append(role)
        db.session.add(user)
        db.session.commit()
        flash("Регистрация успешна. Войдите в систему.", "success")
        return redirect(url_for("auth.login"))
    return render_template("auth/register.html", form=form)


@auth_bp.get("/logout")
@login_required
def logout():
    logout_user()
    flash("Вы вышли из системы", "info")
    return redirect(url_for("public.index"))

