odoo.define("custom_pos.LocationShowup", function (require) {
    "use strict";
    const AbstractAwaitablePopup = require("point_of_sale.AbstractAwaitablePopup");
    const { useState } = owl;
    const Registries = require("point_of_sale.Registries");
    const { _lt } = require('@web/core/l10n/translation');
    const { Order } = require("point_of_sale.models");

    class LocationShowup extends AbstractAwaitablePopup {
        setup() {
            super.setup();
            this.state = useState({ selected_loc: this.props.list.find((item) => item.isSelected) });
        }
        selectItem(itemId) {

            this.state.selected_loc = itemId;
            this.confirm();
        }

        getPayload() {
            const selected = this.props.list.find((item) => this.state.selected_loc === item.id);
            return selected && selected.item;
        }
    }
    LocationShowup.template = "LocationShowup_template"
    LocationShowup.defaultProps = {
        cancelText: _lt('Cancel'),
        title: _lt('Select Customers Location'),
        body: '',
        list: [],
        confirmKey: false,
    }
    Registries.Component.add(LocationShowup)



    const OrderExtendLoc = (Order) => class OrderExtendLoc extends Order {

        export_as_JSON() {
            const json = super.export_as_JSON(...arguments);
            json.selected_location = this.selected_location;
            return json;
        }

        init_from_JSON(json) {
            super.init_from_JSON(...arguments);
            this.set_location(json.selected_location)
        }

        set_location(selected_location) {
            this.selected_location = selected_location
        }

        get_location() {
            if (this.selected_location) {
                return this.selected_location;
            }
        }


    }

    Registries.Model.extend(Order, OrderExtendLoc)

});