/** @odoo-module **/

import publicWidget from 'web.public.widget';

publicWidget.registry.yhEmployees = publicWidget.Widget.extend({
    selector: '.explore-employees',
    start() {
        let employeesRow = this.el.querySelector('#yh-employees-row')
    
        if (employeesRow) {
            this._rpc({
                route: '/Employees/',
                params: {}
            }).then(data => {
                let html = ``;
                for (let i = 0; i < data.length; i++) {
                    if (i % 3 === 0) {
                   
                        html += `<div class="row">`;
                    }
        
                    html += `<div class="col-lg-4 mb-5">
                        <div class="d-flex align-items-center">
                            <div class="img-container mr-3 rounded">
                                <img class="employee-img-container rounded-circle mx-auto" src="data:image/png;base64,${data[i].image}"/>
                            </div>
                            <div>
                                <div><h5 class="mb-0">${data[i].employee_name}</h5></div>
                                <div>Experience: ${data[i].experience}</div>
                                <div>Phone-Number: ${data[i].phone_number}</div>
                                <p class="mb-0">${data[i].state_id ? data[i].state_id[1] : ''}</p>
                            </div>  
                        </div>
                    </div>`;
        
                    if ((i + 1) % 3 === 0 || i === data.length - 1) {
               
                        html += `</div>`;
                    }
                }
        
                employeesRow.innerHTML = html;
            });
        }
        
    },
});

export default publicWidget.registry.yhEmployees;
