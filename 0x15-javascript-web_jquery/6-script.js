#!/usr/bin/node

$(function () {
    $('#update_header').click( () => {
        $('header').text('New Header!!!');
    });
});