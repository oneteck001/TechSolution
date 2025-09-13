from flask import render_template, redirect, url_for, flash
from flask_login import login_required
from . import admin_bp
from ...security import roles_required
from ...models import News, Job
from ...forms import NewsForm, JobForm
from ...extensions import db


@admin_bp.get("/")
@login_required
@roles_required("admin")
def dashboard():
    news_count = News.query.count()
    jobs_count = Job.query.count()
    return render_template("admin/dashboard.html", news_count=news_count, jobs_count=jobs_count)


# Новости
@admin_bp.get("/news")
@login_required
@roles_required("admin")
def news_list():
    items = News.query.order_by(News.created_at.desc()).all()
    return render_template("admin/news_list.html", items=items)


@admin_bp.route("/news/create", methods=["GET", "POST"])
@login_required
@roles_required("admin")
def news_create():
    form = NewsForm()
    if form.validate_on_submit():
        item = News(title=form.title.data, body=form.body.data)
        db.session.add(item)
        db.session.commit()
        flash("Новость создана", "success")
        return redirect(url_for("admin.news_list"))
    return render_template("admin/news_form.html", form=form)


# Вакансии
@admin_bp.get("/jobs")
@login_required
@roles_required("admin")
def jobs_list():
    items = Job.query.order_by(Job.created_at.desc()).all()
    return render_template("admin/jobs_list.html", items=items)


@admin_bp.route("/jobs/create", methods=["GET", "POST"])
@login_required
@roles_required("admin")
def job_create():
    form = JobForm()
    if form.validate_on_submit():
        job = Job(
            title=form.title.data,
            department=form.department.data,
            location=form.location.data,
            employment_type=form.employment_type.data,
            description=form.description.data,
            active=True
        )
        db.session.add(job)
        db.session.commit()
        flash("Вакансия создана", "success")
        return redirect(url_for("admin.jobs_list"))
    return render_template("admin/job_form.html", form=form)

