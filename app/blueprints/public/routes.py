from flask import render_template
from . import public_bp
from app.forms import ContactForm

@public_bp.route("/")
def index():
    return render_template("public/index.html")


@public_bp.route("/about")
def about():
    return render_template("public/about.html")


@public_bp.route("/services")
def services():
    return render_template("public/services.html")


@public_bp.route("/news")
def news_list():
    return render_template("public/news_list.html")


@public_bp.route("/news/<int:news_id>")
def news_detail(news_id):
    return render_template("public/news_detail.html", news_id=news_id)


@public_bp.route("/careers")
def careers():
    return render_template("public/careers.html")


@public_bp.route("/jobs/<int:job_id>")
def job_detail(job_id):
    return render_template("public/job_detail.html", job_id=job_id)

@public_bp.route("/contacts", methods=["GET", "POST"])
def contacts():
    form = ContactForm()
    if form.validate_on_submit():
        # тут можно сделать отправку email, запись в БД и т.п.
        flash("Ваше сообщение успешно отправлено!", "success")
        return redirect(url_for("public.contacts"))
    return render_template("public/contacts.html", form=form)

