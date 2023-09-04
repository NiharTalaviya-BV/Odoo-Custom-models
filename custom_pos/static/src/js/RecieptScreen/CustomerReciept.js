odoo.define('point_of_sale.phone_number', function(require) {
    'use strict';
 
    var { Order } = require('point_of_sale.models');
    const Registries = require('point_of_sale.Registries');
    
    const customerNote = (Order) => class customerNote extends Order {

        export_for_printing(){
        
            var result = super.export_for_printing(...arguments);
            result.customerNote = this.get_customer_order_note();
            result.alternate_phone_num = this.partner.alternate_phone_num;
            return result
        }
    }

    Registries.Model.extend(Order, customerNote);

    return customerNote;
});