from odoo import http


class YourHomeEmployees(http.Controller):

    @http.route('/Employees/', auth="public", type="json", methods=['POST'])
    def all_Employees(self):
        Employees = http.request.env['yh.employees'].search_read([], ['employee_name', 'phone_number', 'experience', 'country_id', 'state_id', 'image'])
        return Employees
