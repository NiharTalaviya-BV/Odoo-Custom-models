odoo.define("custom_pos.Validation", function (require) {
  "use strict";

  const ActionpadWidget = require("point_of_sale.ActionpadWidget");
  const Registries = require("point_of_sale.Registries");
  const PaymentScreen = require("point_of_sale.PaymentScreen");

  const InheritActionpad = (ActionpadWidget) =>
    class InheritActionpad extends ActionpadWidget {
      setup() {
        super.setup();
        console.log(this.env.pos.get_order().partner);
      }
      customerValidation() {
        if (this.env.pos.get_order().partner == null) {
          return this.showPopup("ErrorPopup", {
            title: this.env._t("Customer is not selected!"),
            body: this.env._t(
              "Please select the customer to proceed the order further."
            ),
          });
        }
      }
    };

  Registries.Component.extend(ActionpadWidget, InheritActionpad);

  const PaymentScreenValidation = (PaymentScreen) =>
    class PaymentScreenValidation extends PaymentScreen {
      setup() {
        super.setup();
        console.log(this.env.pos.get_order().partner);
      }
      _isOrderValid(isForceValidate) {
        if (this.env.pos.get_order().partner == null) {
          this.showPopup("ErrorPopup", {
            title: this.env._t("Customer is not selected!"),
            body: this.env._t(
              "Please select the customer to proceed the order further."
            ),
          });
          return false;
        }

        return super._isOrderValid(isForceValidate);
      }
    };
  Registries.Component.extend(PaymentScreen, PaymentScreenValidation);
});
