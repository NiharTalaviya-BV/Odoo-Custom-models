odoo.define('point_of_sale.ExtendedOrder', function(require) {
    'use strict';
 
    var { Order } = require('point_of_sale.models');
    const Registries = require('point_of_sale.Registries');
    
    const ExtendedOrder = (Order) => class ExtendedOrder extends Order {

        constructor() {
            super(...arguments);
            this.customerNote = this.customerNote || '';
        }

        init_from_JSON(json) {
            super.init_from_JSON(json);
            this.set_customer_order_note(json.customer_order_note);
        }

        export_as_JSON() {
            const json = super.export_as_JSON();
            json.customer_order_note = this.get_customer_order_note();
            return json;
        }

        set_customer_order_note(text) {
            this.customerNote = text;
        }

        get_customer_order_note() {
            return this.customerNote;
        }


        export_for_printing(){
        
            var result = super.export_for_printing(...arguments);
            result.customerNote = this.get_customer_order_note();
            result.alternate_phone_num = this.partner.alternate_phone_num;
            return result
        }

       
    }
    
    Registries.Model.extend(Order, ExtendedOrder);

    return ExtendedOrder;
});