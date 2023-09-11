from odoo import http
from odoo.http import request

class XLSXReportController(http.Controller):
    @http.route('/web/content/<string:model>/<int:res_id>/xls_report', type='http', auth='user')
    def download_xlsx_report(self, model, res_id):
        record = request.env[model].sudo().browse(res_id)
        return request.make_response(record.xls_report, [('Content-Type', 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')])
