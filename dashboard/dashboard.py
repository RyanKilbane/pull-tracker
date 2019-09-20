from flask import render_template, request, Blueprint

dashboard_blueprint = Blueprint(name="dashboard",import_name=__name__, url_prefix="/")

@dashboard_blueprint.route("/")
def dashboard():
    print("Reached dash")
    return render_template("dashboard.html")