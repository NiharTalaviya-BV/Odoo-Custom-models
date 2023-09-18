$(function () {
    $('#candidateForm').submit(function (e) {
            
              $.ajax({
                type: 'post',
                url: '/create/candidate',
                data: $(this).serialize(),
              });
          e.preventDefault();
        });
});

odoo.define('your_company.checkLogin', function (require) {
    'use strict';

    var publicWidget = require('web.public.widget');
    var session = require('web.session'); 

    publicWidget.registry.yourSubmitButton = publicWidget.Widget.extend({
        selector: '.btn-form-submit',
        events: {
            'click': '_onClickSubmit',
        },

        _onClickSubmit: function () {
            var self = this;
    
            if (!this.getSession().user_id) {
                console.log(session.uid)
                self.showPopup("You are not logged in! Please log in to submit your application.");
            }
            else {
                self.showSuccessPopup("Your Data is successfully sent to the company!");
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
