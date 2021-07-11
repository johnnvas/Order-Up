from flask import Blueprint
from flask_login import login_required

bp = Blueprint("orders", __name__, url_prefix="")


# Make your index function look like this
@bp.route("/")
@login_required
def index():
    return "Order Up!"
