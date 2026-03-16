from flask import jsonify, Blueprint

users_bp = Blueprint('users', __name__, url_prefix='/api/users')

@users_bp.route("/", methods=['GET'])
def index():
    return jsonify({"message": "ok"})
