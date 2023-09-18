// odoo.define('custom_pos.override', function (require) {
//     'use strict';
//     const Registries = require('point_of_sale.Registries');
//     const Orderline = require('point_of_sale.Orderline');
//     var core = require('web.core');
//     var _t = core._t;
//       const WidgetsOverride = (Orderline) =>
//           class extends Orderline {
//               selectLine()  {
               
//                   const line = this.props.line;
//                   console.log(line)
//                   const { confirmed } =  this.showPopup('ConfirmPopup', {
//                            title: this.env._t(line.product.display_name),
//                            body: _.str.sprintf(this.env._t('Name : %s - invoice_policy : %s'), line.product.lst_price,
//                            line.product.invoice_policy),
                           
//                    });
//                    console.log("it's running")  
//               }
//        };
//       Registries.Component.extend(Orderline, WidgetsOverride);
//      return Orderline;
//     }); 