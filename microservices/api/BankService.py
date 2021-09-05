from Utility import Utility
from flask import jsonify, app
from flask import request

from api import bp
from Bank import Bank
from Utility import Utility

def check_parameters(req, params):
    missing = []
    for param in params:
        if not param in req:
            missing.append("%s is required" % param)
    return missing

@bp.route('/', methods=['GET'])
def root():
    return jsonify({"success": True, "message": "Service Available"}), 200

@bp.route('/transfer', methods=['POST'])
def transfer():
    util = Utility()
    bank = Bank()
    if request.method == 'POST':
        util.info(f"initiate transfer")

        if request.headers['Content-Type'] == 'application/json':
            req_data = request.get_json()
            util.debug(req_data)
            response = bank.transfer()
            response['success'] = True
            return jsonify(response), 200
        else:
            return jsonify({"success": False, "message": "415 Unsupported Media Type"}), 415

@bp.route('/debit', methods=['POST'])
def debit():
    util = Utility()
    bank = Bank()
    if request.method == 'POST':
        util.info(f"initiate debit")

        if request.headers['Content-Type'] == 'application/json':
            req_data = request.get_json()
            util.debug(req_data)
            response = bank.debit()
            response['success'] = True
            return jsonify(response), 200
        else:
            return jsonify({"success": False, "message": "415 Unsupported Media Type"}), 415

@bp.route('/cashin', methods=['POST'])
def cashin():
    util = Utility()
    bank = Bank()
    if request.method == 'POST':
        util.info(f"initiate cashin")

        if request.headers['Content-Type'] == 'application/json':
            req_data = request.get_json()
            util.debug(req_data)
            response = bank.cashin()
            response['success'] = True
            return jsonify(response), 200
        else:
            return jsonify({"success": False, "message": "415 Unsupported Media Type"}), 415

@bp.route('/cashout', methods=['POST'])
def caschout():
    util = Utility()
    bank = Bank()
    if request.method == 'POST':
        util.info(f"initiate cashout")

        if request.headers['Content-Type'] == 'application/json':
            req_data = request.get_json()
            util.debug(req_data)
            response = bank.cashout()
            response['success'] = True
            return jsonify(response), 200
        else:
            return jsonify({"success": False, "message": "415 Unsupported Media Type"}), 415

@bp.route('/payment', methods=['POST'])
def payment():
    util = Utility()
    bank = Bank()
    if request.method == 'POST':
        util.info(f"initiate payment")

        if request.headers['Content-Type'] == 'application/json':
            req_data = request.get_json()
            util.debug(req_data)
            response = bank.payment()
            response['success'] = True
            return jsonify(response), 200
        else:
            return jsonify({"success": False, "message": "415 Unsupported Media Type"}), 415            