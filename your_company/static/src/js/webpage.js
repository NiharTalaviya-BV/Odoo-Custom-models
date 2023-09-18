odoo.define('your_company.checkLogin', function (require) {
    'use strict';

    var publicWidget = require('web.public.widget');
    var session = require('web.session'); 

    publicWidget.registry.yourSubmitButton = publicWidget.Widget.extend({
        selector: '.btn-form-submit',
        events: {
            'click': '_onClickSubmit',
        },

        _onClickSubmit: function (ev) {
            ev.preventDefault(); 

            var self = this;
            var formElement = this.$el.closest('form')[0];

            if (formElement && formElement instanceof HTMLFormElement) {
                var formData = new FormData(formElement);

                $.ajax({
                    type: 'post',
                    url: '/create/candidate',
                    data: formData,
                    processData: false,
                    contentType: false,
                    success: function (data) {
                
                        console.log('Data saved successfully', data);

                    
                        if (!self.getSession().user_id) {
                            console.log(session.uid)
                            self.showPopup("You are not logged in! Please log in to submit your application.");
                        }
                        else {
                            self.showSuccessPopup("Your Data is successfully sent to the company!");
                        }
                    },
                    error: function (errorThrown) {
                        console.error('Error:', errorThrown, formData);
                    },
                });
            } else {
                console.error('Form element not found or is not a <form> element');
            }
        },

        showPopup: function (message) {

            var modal = $('<div class="modal fade" tabindex="-1" role="dialog">' +
                '<div class="modal-dialog" role="document">' +
                '<div class="modal-content">' +
                '<div class="modal-header">' +
                '<h5 class="modal-title">Login Required</h5>' +
                '<button type="button" class="close" data-dismiss="modal" aria-label="Close">' +
                '<span aria-hidden="true">&times;</span>' +
                '</button>' +
                '</div>' +
                '<div class="modal-body">' +
                '<p>' + message + '</p>' +
                '</div>' +
                '<div class="modal-footer">' +
                '<button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button>' +
                '<a class="btn btn-primary" href="/web/login">Log In</a>' +
                '</div>' +
                '</div>' +
                '</div>' +
                '</div>');

            modal.modal('show');

            
            modal.on('hidden.bs.modal', function () {
                modal.remove(); 
            });
        },

        showSuccessPopup: function (message) {
  
            var modal = $('<div class="modal fade" tabindex="-1" role="dialog">' +
                '<div class="modal-dialog" role="document">' +
                '<div class="modal-content">' +
                '<div class="modal-header">' +
                '<h5 class="modal-title">Success</h5>' +
                '<button type="button" class="close" data-dismiss="modal" aria-label="Close">' +
                '<span aria-hidden="true">&times;</span>' +
                '</button>' +
                '</div>' +
                '<div class="modal-body">' +
                '<p>' + message + '</p>' +
                '</div>' +
                '<div class="modal-footer">' +
                '<button type="button" class="btn btn-primary" data-dismiss="modal">Close</button>' +
                '</div>' +
                '</div>' +
                '</div>' +
                '</div>');

            modal.modal('show');


            modal.on('hidden.bs.modal', function () {
                modal.remove(); 
            });
        },
    });
});
