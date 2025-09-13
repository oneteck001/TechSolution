from flask import render_template, request, redirect, url_for, flash
from . import public_bp
from ...models import News, Service, Job, ContactMessage
from ...forms import ContactForm, JobApplicationForm
from ...extensions import db

@public_bp.get('/')
def index():
news = News.query.filter_by(published=True).order_by(News.created_at.desc()).limit(3).all()
services = Service.query.limit(6).all()
jobs = Job.query.filter_by(active=True).order_by(Job.created_at.desc()).limit(3).all()
return render_template('public/index.html', news=news, services=services, jobs=jobs)

@public_bp.get('/about')
def about():
return render_template('public/about.html')

@public_bp.get('/services')
def services():
items = Service.query.all()
return render_template('public/services.html', services=items)

@public_bp.get('/news')
def news_list():
items = News.query.filter_by(published=True).order_by(News.created_at.desc()).all()
return render_template('public/news_list.html', items=items)

@public_bp.get('/news/<int:news_id>')
def news_detail(news_id):
item = News.query.get_or_404(news_id)
if not item.published:
flash('Новость недоступна', 'warning')
return redirect(url_for('public.news_list'))
return render_template('public/news_detail.html', item=item)

@public_bp.get('/careers')
def careers():
jobs = Job.query.filter_by(active=True).order_by(Job.created_at.desc()).all()
return render_template('public/careers.html', jobs=jobs)

@public_bp.route('/jobs/<int:job_id>', methods=['GET', 'POST'])
def job_detail(job_id):
job = Job.query.get_or_404(job_id)
form = JobApplicationForm()
if form.validate_on_submit():
from ...models import JobApplication
app = JobApplication(job_id=job.id, name=form.name.data, email=form.email.data,
phone=form.phone.data, message=form.message.data)
db.session.add(app)
db.session.commit()
flash('Заявка отправлена! Мы свяжемся с вами.', 'success')
return redirect(url_for('public.careers'))
return render_template('public/job_detail.html', job=job, form=form)

@public_bp.route('/contacts', methods=['GET', 'POST'])
def contacts():
form = ContactForm()
if form.validate_on_submit():
msg = ContactMessage(name=form.name.data, email=form.email.data,
subject=form.subject.data, message=form.message.data)
db.session.add(msg)
db.session.commit()
flash('Сообщение отправлено. Спасибо!', 'success')
return redirect(url_for('public.contacts'))
return render_template('public/contacts.html', form=form)
