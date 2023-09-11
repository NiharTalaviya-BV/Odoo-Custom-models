odoo.define('custom_pos.customerNotePopup', function (require) {
    'use strict';
    const TextAreaPopup = require('point_of_sale.TextAreaPopup');
    const models = require('point_of_sale.models')
    const Registries = require('point_of_sale.Registries');
    const { useState, useRef } = owl;
    const { _lt } = require('@web/core/l10n/translation');

    class customerNotePopup extends TextAreaPopup {
        /**
         * @param {Object} props
         * @param {string} props.startingValue
         */
        setup() {
            
            super.setup();
           
            this.state =  useState({ inputValue: this.props.startingValue });
            this.customerNote = useRef('customerNote');
            
            this.phone = useState({
                error: '',  
            }); 
        }

        getPayload() {
            return this.state.inputValue;
        }

      
       
    }
    customerNotePopup.template = 'custom_pos.customerNotePopup';
   
    Registries.Component.add(customerNotePopup);

    return customerNotePopup;

});

