from flask import render_template
from flask_login import login_required, current_user
from . import dashboard_bp


@dashboard_bp.get("/dashboard")
@login_required
def index():
    return render_template("dashboard/index.html", user=current_user)

