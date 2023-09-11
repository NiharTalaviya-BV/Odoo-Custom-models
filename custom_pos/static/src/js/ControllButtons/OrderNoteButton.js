odoo.define('custom_pos', function(require) {
    'use strict';

    var { Order } = require('point_of_sale.models');
    const ProductScreen = require('point_of_sale.ProductScreen');
    const Registries = require('point_of_sale.Registries');
    const { Gui } = require('point_of_sale.Gui');

    const customerNoteButton = (ProductScreen) => class extends ProductScreen{
        setup() {
            super.setup();
        }
        async onClick() {
            console.log(this.env.pos.get_order())
            const selectedOrder = this.env.pos.get_order();
            const { confirmed, payload: customerNote } = await Gui.showPopup("customerNotePopup", {
                startingValue: selectedOrder.get_customer_order_note(),
                'title': "Add Order Note",
          
            }); 
            if (confirmed) {
                selectedOrder.set_customer_order_note(customerNote);
                // console.log(confirmed)
            }
        }
    }
    
    
    customerNoteButton.template = 'customerNoteButton';
    Registries.Component.extend(ProductScreen, customerNoteButton);

    return customerNoteButton;

}); 



