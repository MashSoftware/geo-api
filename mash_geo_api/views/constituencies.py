from flask import Response, Blueprint
from mash_geo_api.models import Constituency

constituencies_bp = Blueprint('constituencies', __name__)


@constituencies_bp.route('/', methods=["GET"])
def constituencies():
    constituencies = Constituency.query.all()
    return Response(repr(constituencies), mimetype='application/json')


@constituencies_bp.route('/<id>', methods=["GET"])
def constituency(id):
    constituency = Constituency.query.get(id)
    return Response(repr(constituency), mimetype='application/json')