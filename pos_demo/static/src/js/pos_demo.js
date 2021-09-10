//Se confirma la carga del JS
console.log('JavaScript cargado correctamente');

//Agregar botón de descuento
odoo.define('pos_demo.custom', function (require) {
    "use strict";
    //Se crean constantes que se enlacan a los componentes
    const PosComponent = require('point_of_sale.PosComponent');
    const ProductScreen = require('point_of_sale.ProductScreen');
    const Registries = require('point_of_sale.Registries');
    const pos_model = require('point_of_sale.models');

    pos_model.load_fields("product.product", ["standard_price"]);

    //Funcionalidad del botón
    class PosDiscountButton extends PosComponent {
        async onClick() {
            const order = this.env.pos.get_order();
            if (order.selected_orderline) {
                order.selected_orderline.set_discount(5);
            }
        }
    }
    //Se elige el template para el botón
    PosDiscountButton.template = 'PosDiscountButton';
    //Se muestra el botón en pantalla
    ProductScreen.addControlButton({
        component: PosDiscountButton,
        condition: function () {
            return true;
        },
    });
    //Se registra el botón en los componentes
    Registries.Component.add(PosDiscountButton);



    //Funcionalidad para listar los  últimos 5 pedidos
    class PosLastOrderButton extends PosComponent {
        async onClick() {
            var self = this;
            const order = this.env.pos.get_order();
            if (order.attributes.client) {
                var domain = [['partner_id', '=', order.
                    attributes.client.id]];
                this.rpc({
                    model: 'pos.order', method: 'search_read',
                    args: [domain, ['name', 'amount_total']],
                    kwargs: { limit: 5 },
                }).then(function (orders) {
                    if (orders.length > 0) {
                        var order_list = _.map(orders, function
                            (o) {
                            return {
                                'label': _.str.sprintf("%s - TOTAL: % s", o.name, o.amount_total)
                            };
                        });
                        self.showPopup('SelectionPopup', {
                            title:
                                'Last 5 orders', list: order_list
                        });
                    } else {
                        self.showPopup('ErrorPopup', {
                            body: 'No previous orders found'
                        });
                    }
                });
            } else {
                self.showPopup('ErrorPopup', {
                    body: 'Please select the customer'
                });
            }
        }
    }
    PosLastOrderButton.template = 'PosLastOrderButton';
    ProductScreen.addControlButton({
        component: PosLastOrderButton,
        condition: function () {
            return true;
        },
    });
    Registries.Component.add(PosLastOrderButton);


    return PosDiscountButton;

});


