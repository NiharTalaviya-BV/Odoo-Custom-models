from odoo import http
from odoo.http import request


class YourHomeEmployees(http.Controller):

    @http.route('/Employees/', auth="public", type="json", methods=['POST'])
    def all_Employees(self):
        Employees = http.request.env['yh.employees'].search_read(
            [], ['employee_name', 'phone_number', 'experience', 'country_id', 'state_id', 'image'])
        return Employees

    @http.route('/custom_page', type='http', auth="user", website=True)
    def custom_page(self):
        return request.render('your_company.custom_homepage')

    @http.route('/create/candidate', type='http', auth="user", website=True)
    def create_candidate(self, **kw):
        print("Form Data:", kw)
        request.env['yh.candidate'].sudo().create(kw)
        return request.render('your_company.custom_homepage')
