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
            console.log()
            const selectedOrder = this.env.pos.get_order();
            const { confirmed, payload: customerNote } = await Gui.showPopup("TextAreaPopup", {
                startingValue: selectedOrder.get_customer_order_note(),
                'title': "Add Order Note",
                // 'body':  `${this.env.pos.get_order().partner.name} is selected`,
            });
            // console.log("clicked")
            // const selectedOrder = this.env.pos.get_order();
            // const { confirmed, payload: phoneNumber } = await this.showPopup('PhoneNumberPopup',  {
            //     startingValue: selectedOrder.get_customer_phone_number(),
            //     title: this.env._t('Add Customer Phone Number'),
            // });
            if (confirmed) {
                selectedOrder.set_customer_order_note(customerNote);
            }
        }
    }
    
    
    customerNoteButton.template = 'customerNoteButton';
    Registries.Component.extend(ProductScreen, customerNoteButton);

    return customerNoteButton;

    

}); 



