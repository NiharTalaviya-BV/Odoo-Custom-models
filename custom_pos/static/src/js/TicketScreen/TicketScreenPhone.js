odoo.define('custom_pos.Ticket', function(require) {
    'use strict';
 
    const TicketScreen = require('point_of_sale.TicketScreen');
    const Registries = require('point_of_sale.Registries');
    const { useState } = owl;

    const CustomTicketScreen = (TicketScreen) =>
    class CustomTicketScreen extends TicketScreen {
        setup() {
            super.setup();
            const customer_note = this.env.pos.get_order().get_customer_order_note();
            this.customer_note = useState({'note': customer_note})
            console.log(this.env.pos.get_order().get_customer_order_note());
        }
    }

    Registries.Component.extend(TicketScreen, CustomTicketScreen);

    return CustomTicketScreen;
});
