odoo.define('custom_pos.PosGlobalLocation', function (require) {
    'use strict';

    const { PosGlobalState } = require('point_of_sale.models');
    const Registries = require('point_of_sale.Registries');
    
    const PosGlobalLocation = (PosGlobalState) => class extends PosGlobalState {


        async _processData(loadedData) {
            await super._processData(loadedData)
            this.LOCATIONS = loadedData['store.location'] || [];
            this.store_locations = loadedData['location_name']
        }
    }
    
    Registries.Model.extend(PosGlobalState,PosGlobalLocation);

});