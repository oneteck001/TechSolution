from flask import Flask, render_template
from .extensions import db, migrate, login_manager, csrf
from .models import User, Role
from .blueprints.public.routes import public_bp
from .blueprints.auth.routes import auth_bp
from .blueprints.dashboard.routes import dashboard_bp
from .blueprints.admin.routes import admin_bp
from .models import News, Service, Job


def create_app():
    app = Flask(__name__, static_folder="static", template_folder="templates")
    app.config.from_object("config.Config")

    # init extensions
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)
    csrf.init_app(app)

    # 👇 вот это добавь
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    # blueprints
    app.register_blueprint(public_bp)
    app.register_blueprint(auth_bp, url_prefix="/auth")
    app.register_blueprint(dashboard_bp)
    app.register_blueprint(admin_bp, url_prefix="/admin")

    # context
    @app.context_processor
    def inject_org():
        return {"ORG": app.config.get("ORGANIZATION_NAME", "Ваша Компания")}

    # errors
    @app.errorhandler(404)
    def page_not_found(e):
        return render_template("errors/404.html"), 404

    @app.errorhandler(500)
    def server_error(e):
        return render_template("errors/500.html"), 500

    return app

